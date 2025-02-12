from django.shortcuts import render
from django.shortcuts import render


def catalog_view_home(request):
    return render(request, 'catalog/home.html')


def catalog_view_contacts(request):
    return render(request, 'catalog/contacts.html')


def item_view(request):

    return render(request, 'catalog/item.html')
