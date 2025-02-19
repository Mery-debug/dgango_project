from django.shortcuts import render, get_object_or_404
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


class CatalogViewDetail(DetailView):
    model = get_object_or_404(Product, pk=Product.id)
    context_object_name = 'product'
    template_name = 'catalog/product.html'
    success_url = reverse_lazy('product_details')


class CatalogCreateView(CreateView):
    model = Product
    fields = ['id', 'name', 'description', 'category', 'price', 'img']
    template_name = 'catalog/create.html'
    success_url = reverse_lazy('product_create')


class CatalogUpdateView(UpdateView):
    model = get_object_or_404(Product, pk=Product.id)
    fields = ['name', 'description', 'category', 'price', 'img']
    template_name = 'catalog/update.html'
    success_url = reverse_lazy('product_update')


class CatalogDeleteView(DeleteView):
    model = get_object_or_404(Product, pk=Product.id)
    template_name = 'catalog/confirm_delete.html'
    success_url = reverse_lazy('product_list')

