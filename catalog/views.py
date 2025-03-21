from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, View

from .forms import ProductForm
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
    form_class = ProductForm
    context_object_name = "products"
    template_name = "authorization/products.html"
    success_url = reverse_lazy("authorization:product_list")

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


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


class CatalogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.Product'
    model = Product
    form_class = ProductForm
    template_name = "authorization/create_product.html"
    success_url = reverse_lazy("authorization:product_detail")

    def get_success_url(self):
        return reverse_lazy(
            "authorization:product_detail", kwargs={"pk": self.object.pk}
        )

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product = get_object_or_404(*args, **kwargs)

            if not request.user.has_perm('product.can_unpublish_product'):
                return HttpResponseForbidden('Не достаточно прав для публикации нового товара, зарегистрируйтесь или '
                                             'войди в аккаунт.')
            form = ProductForm
            product.save()
            if form.is_valid:
                product = form.save(commit=False)
                product.owner = request.user
                product.save()
                return redirect('authorization:product_list')
        else:
            form = ProductForm()
        return render(request, 'authorization/create_product.html', {'form': form})


class CatalogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.Product'
    model = Product
    form_class = ProductForm
    template_name = "authorization/update_spam.html"
    success_url = reverse_lazy("authorization:product_detail")

    def get_success_url(self):
        return reverse_lazy(
            "authorization:product_detail", kwargs={"pk": self.object.pk}
        )


class CatalogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.Product'
    model = Product
    template_name = "authorization/confirm_delete.html"
    success_url = reverse_lazy("authorization:product_list")

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(*args, **kwargs)

        if not request.user.has_perm('product.can_delete_product'):
            return HttpResponseForbidden('Не достаточно прав для удаления товара, зарегистрируйтесь или '
                                         'войди в аккаунт.')
        product.delete()
        return redirect('catalog:product_list')
