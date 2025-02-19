from django.views.generic.edit import CreateView, UpdateView, View, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy, reverse
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
    success_url = reverse_lazy('product_list/')


class CatalogViewDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'catalog/product.html'
    success_url = reverse_lazy('product_details/')


class CatalogCreateView(CreateView):
    model = Product
    fields = ['id', 'name', 'descriptions', 'category', 'price']
    template_name = 'catalog/create.html'
    success_url = reverse_lazy('product_list/')


class CatalogUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'category', 'price', 'img']
    template_name = 'catalog/update.html'
    success_url = reverse_lazy('product/<int:pk>/edit/')


class CatalogDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/confirm_delete.html'
    success_url = reverse_lazy('product_list/')

