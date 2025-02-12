from django.shortcuts import render
from django.shortcuts import render

from catalog.models import Product


def catalog_view_home(request):
    return render(request, 'catalog/home.html')


def catalog_view_contacts(request):
    return render(request, 'catalog/contacts.html')


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/products.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'catalog/product.html', context)

