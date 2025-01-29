from django.shortcuts import render
from django.http import HttpResponse


def catalog_view_home(request):
    return render(request, 'catalog/home.html')


def catalog_view_contacts(request):
    return render(request, 'catalog/contacts.html')
