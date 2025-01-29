from django.shortcuts import render
# from django.http import HttpResponse


def catalog_view_home(request):
    return render(request, 'catalog/home.html')


def catalog_view_contacts(request):
    return render(request, 'catalog/contacts.html')


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
#     return render(request, 'students/contact.html')
