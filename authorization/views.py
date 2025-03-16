import os

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from config.settings import EMAIL_HOST_USER
from .forms import AuthForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.contrib.auth import login
from dotenv import load_dotenv


class AuthRegister(FormView):
    template_name = 'authorization/register.html'
    form_class = AuthForm
    success_url = reverse_lazy('authorization:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать,'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        load_dotenv()
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


class AuthHome(TemplateView):
    template_name = 'authorization/home.html'
    success_url = reverse_lazy('authorization:home')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CustomLogoutView(View):
    template_name = 'authorization/goodbye.html'
    success_url = reverse_lazy('authorization:goodbye')

    def get(self, request):
        return render(request, 'authorization/goodbye.html')


class CustomLoginView(LoginView):
    template_name = 'authorization/login.html'
    success_url = reverse_lazy('authorization:home')
