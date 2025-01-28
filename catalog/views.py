from django.shortcuts import render


def catalog_view_home(request):
    return render(request, 'app/home.html')


def catalog_view_contacts(request):
    return render(request, 'app/contacts.html')
