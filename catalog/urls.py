from django.contrib import admin
from django.urls import path
from catalog import views

app_name = 'catalog'


urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/', views.catalog_view_home, name='catalog_view_home'),
    path('contacts/', views.catalog_view_contacts, name='catalog_view_contacts'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),
]