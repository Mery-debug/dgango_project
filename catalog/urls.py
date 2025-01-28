from django.contrib import admin
from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.catalog_view_home, name='catalog_view_home'),
    path('', views.catalog_view_contacts, name='catalog_view_contacts'),
]
