from django.views.generic.edit import CreateView, UpdateView, View, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Product


class CatalogHomeView(View):
    template_name = 'catalog/home.html'
    success_url = reverse_lazy('home')


class CatalogContactsView(View):
    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('contacts')


class CatalogViewList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'catalog/products.html'
    success_url = reverse_lazy('product_list')

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class CatalogViewDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'catalog/product.html'
    success_url = reverse_lazy('product_details')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'].img = getattr(context['product'], 'img', None)
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.is_active:
            obj.view_count += 1
            obj.save()
            return obj
        else:
            return None


class CatalogCreateView(CreateView):
    model = Product
    fields = ['id', 'name', 'descriptions', 'category', 'price', 'img']
    template_name = 'catalog/create.html'
    success_url = reverse_lazy('catalog:product_list')


class CatalogUpdateView(UpdateView):
    model = Product
    fields = ['name', 'descriptions', 'category', 'price', 'img']
    template_name = 'catalog/update.html'
    success_url = reverse_lazy('product/<int:pk>/edit/')


class CatalogDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

