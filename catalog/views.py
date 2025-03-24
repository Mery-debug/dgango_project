from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, View

from .forms import ProductForm, ProductModeratorForm
from .models import Product


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
        if user.groups.filter(name='Moder').exists():
            return Product.objects.all()
        return Product.objects.filter(is_published=True)


class CatalogViewDetail(DetailView):
    model = Product
    form_class = ProductForm
    template_name = "authorization/product.html"
    success_url = reverse_lazy("product_details")

    def get_success_url(self):
        return reverse_lazy(
            "authorization:product_detail", kwargs={"pk": self.object.pk}
        )

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


class CatalogCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "authorization/create_product.html"

    def get_success_url(self):
        return reverse_lazy(
            "authorization:product_detail", kwargs={"pk": self.object.pk}
        )

    def has_permission(self):
        return self.request.user.groups.filter(name="moder").exists()

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CatalogUpdateView(UpdateView):
    model = Product
    template_name = "authorization/update_product.html"
    success_url = reverse_lazy("authorization:product_detail")

    def get_success_url(self):
        return reverse_lazy(
            "authorization:product_detail", kwargs={"pk": self.object.pk}
        )

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.groups.filter(name='Moder').exists():
            return ProductModeratorForm
        raise PermissionDenied


class CatalogDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("authorization:product_list")

    def get_template_names(self):
        user = self.request.user
        if user == self.object.owner or user.groups.filter(name='Moder').exists():
            return "authorization/confirm_delete.html"
        raise PermissionDenied

