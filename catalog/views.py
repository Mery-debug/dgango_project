from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, View
from django.core.cache import cache

from config.settings import MODERATOR_GROUP
from .forms import ProductForm, ProductModeratorForm
from .models import Product, Category
from authorization.servicies import CategoryProduct


class CatalogHomeView(View):
    template_name = "catalog/home.html"
    success_url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CatalogContactsView(View):
    template_name = "catalog/contacts.html"
    success_url = reverse_lazy("contacts")

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CatalogViewList(ListView):
    model = Product
    context_object_name = "products"
    template_name = "authorization/products.html"
    success_url = reverse_lazy("authorization:product_list")

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name=MODERATOR_GROUP).exists():
            return Product.objects.all()
        queryset = cache.get('published_products')
        if not queryset:
            queryset = Product.objects.filter(is_published=True)
            cache.set('published_products', queryset, 60 * 15)  # Кеш на 15 минут
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import Category
        context['categories'] = Category.objects.all()
        if hasattr(self.request, 'category'):
            context['current_category'] = self.request.category
        return context


@method_decorator(cache_page(60 * 15), name='dispatch')
class CatalogViewDetail(DetailView):
    model = Product
    template_name = "authorization/product.html"

    def get_success_url(self):
        return reverse_lazy(
            "authorization:product_detail", kwargs={"pk": self.object.pk}
        )

    def get_form_class(self):
        user = self.request.user
        if user.groups.filter(name=MODERATOR_GROUP).exists():
            return ProductModeratorForm
        return ProductForm

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name=MODERATOR_GROUP).exists():
            return Product.objects.all()
        return Product.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"].img = getattr(context["product"], "img", None)
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.is_active:
            obj.view_count += 1
            obj.save()
            return obj
        else:
            return None


class CatalogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "authorization/create_product.html"

    def get_success_url(self):
        return reverse_lazy("authorization:product_list")

    def has_permission(self):
        if not self.request.user.groups.filter(name=MODERATOR_GROUP).exists():
            return self.request.user.is_active

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CatalogUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "authorization/update_product.html"
    success_url = reverse_lazy("authorization:product_detail")

    def get_success_url(self):
        return reverse_lazy("authorization:product_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.groups.filter(name=MODERATOR_GROUP).exists():
            return ProductModeratorForm
        raise PermissionDenied


class CatalogDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("authorization:product_list")

    def get_template_names(self):
        user = self.request.user
        if user == self.object.owner or user.groups.filter(name=MODERATOR_GROUP).exists():
            return "authorization/confirm_delete.html"
        raise PermissionDenied


@method_decorator(cache_page(60), name="dispatch")
class CategoryView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "authorization/products.html"
    context_object_name = "products"

    def get_queryset(self):
        category_pk = self.kwargs.get('pk')
        queryset = super().get_queryset()
        if category_pk:
            queryset = queryset.filter(category__pk=category_pk)
        if not self.request.user.groups.filter(name=MODERATOR_GROUP).exists():
            queryset = queryset.filter(is_published=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_pk = self.kwargs.get('pk')
        if category_pk:
            context['current_category'] = Category.objects.get(pk=category_pk)
        return context

