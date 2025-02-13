from django.shortcuts import render, get_object_or_404

from .models import Product


def catalog_view_home(request):
    return render(request, 'catalog/home.html')


def catalog_view_contacts(request):
    return render(request, 'catalog/contacts.html')


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/products.html', context)


def product_detail(request, product_id=Product.id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'catalog/product.html', context)

