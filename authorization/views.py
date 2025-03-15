from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import AuthForm
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy


class AuthRegister(CreateView):
    template_name = 'authorization/register.html'
    form_class = AuthForm
    redirect_url = reverse_lazy('authorization:home')


class AuthHome(TemplateView):
    template_name = 'authorization/home.html'
    success_url = reverse_lazy('authorization:home')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('goodbye')


class CustomLoginView(LoginView):
    template_name = 'authorization/login.html'
    success_url = reverse_lazy('authorization:home')
