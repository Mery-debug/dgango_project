from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, View

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
        return Product.objects.filter(is_published=True)


@method_decorator(cache_page(60 * 15), name='dispatch')
class CatalogViewDetail(DetailView):
    model = Product
    template_name = "authorization/product.html"
    success_url = reverse_lazy("product_details")

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


class CategoryView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = "authorization/category.html"

    def get_success_url(self):
        return reverse_lazy(
            "authorization:category_list", kwargs={"pk": self.object.id}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.object.id
        context["category"] = CategoryProduct.category_product(category_id)
        return context

