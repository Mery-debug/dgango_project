from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from .forms import AuthForm


class AuthRegister(CreateView):
    template_name = 'authorization/register.html'
    form_class = AuthForm
    success_url = reverse_lazy('home')


class AuthHome(View):
    template_name = 'templates/home.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

