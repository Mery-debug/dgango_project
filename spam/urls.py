from django.contrib import admin
from django.urls import path
from .views import SpamListView, SpamCreateView, SpamDeleteView, SpamDetailView, SpamUpdateView

app_name = 'spam'


urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/', SpamListView.as_view(), name='home'),
    path('spam_detail/<int:pk>/', SpamDetailView.as_view(), name='spam_detail'),
    path('create/', SpamCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', SpamDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', SpamUpdateView.as_view(), name='update'),
]
