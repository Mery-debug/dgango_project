from django.views.generic.edit import CreateView, UpdateView, View, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Spam


class SpamListView(ListView):
    model = Spam
    context_object_name = 'spam'
    template_name = 'spam/home.html'
    success_url = reverse_lazy('home')


class SpamDetailView(DetailView):
    model = Spam
    context_object_name = 'content'
    template_name = 'spam/page.html'
    success_url = reverse_lazy('spam_details')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.is_active:
            obj.view_count += 1
            obj.save()
            return obj
        else:
            return None


class SpamCreateView(CreateView):
    model = Spam
    fields = ['name', 'content', 'img']
    template_name = 'spam/create.html'
    success_url = reverse_lazy('spam:home')


class SpamUpdateView(UpdateView):
    model = Spam
    fields = ['name', 'content', 'img']
    template_name = 'spam/update.html'
    success_url = reverse_lazy('spam:home')


class SpamDeleteView(DeleteView):
    model = Spam
    template_name = 'spam/confirm_delete.html'
    success_url = reverse_lazy('spam:spam_list')

