from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from .forms import AuthForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class AuthRegister(CreateView):
    template_name = 'authorization/register.html'
    form_class = AuthForm
    success_url = reverse_lazy('home')


class AuthHome(View):
    template_name = 'authorization/home.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

