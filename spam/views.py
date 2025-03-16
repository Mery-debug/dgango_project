from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from spam.models import Spam


class SpamListView(ListView):
    model = Spam
    context_object_name = "spams"
    template_name = "authorization/contents.html"
    success_url = reverse_lazy("authorization:spam_list")

    def get_queryset(self):
        return Spam.objects.filter(is_active=True)


class SpamDetailView(DetailView):
    model = Spam
    context_object_name = "spam"
    template_name = "authorization/content.html"
    success_url = reverse_lazy("authorization:spam_details")

    def get_success_url(self):
        return reverse_lazy("authorization:spam_detail", kwargs={"pk": self.object.pk})

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.is_active:
            obj.view_count += 1
            obj.save()
            return obj
        else:
            return obj


class SpamCreateView(CreateView):
    model = Spam
    fields = ["id", "name", "content", "img"]
    template_name = "authorization/create_spam.html"
    success_url = reverse_lazy("authorization:spam_detail")

    def get_success_url(self):
        return reverse_lazy("authorization:spam_detail", kwargs={"pk": self.object.pk})


class SpamUpdateView(UpdateView):
    model = Spam
    fields = ["name", "content", "img"]
    template_name = "authorization/update_spam.html"
    success_url = reverse_lazy("authorization:spam_detail")

    def get_success_url(self):
        return reverse_lazy("authorization:spam_detail", kwargs={"pk": self.object.pk})


class SpamDeleteView(DeleteView):
    model = Spam
    template_name = "authorization/confirm_delete.html"
    success_url = reverse_lazy("authorization:spam_list")


class SpamHomeView(View):
    template_name = "spam/home.html"
    success_url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
