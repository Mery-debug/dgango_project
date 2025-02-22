from django.contrib import admin
from django.urls import path
from .views import CatalogContactsView, CatalogHomeView, CatalogCreateView, CatalogDeleteView, CatalogUpdateView, \
    CatalogViewDetail, CatalogViewList

app_name = 'catalog'


urlpatterns = [
    path("admin/", admin.site.urls),
    path('product_list/', CatalogViewList.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', CatalogViewDetail.as_view(), name='product_detail'),
    path('product/new/', CatalogCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', CatalogUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', CatalogDeleteView.as_view(), name='product_delete'),
    path('contacts/', CatalogContactsView.as_view(), name='contacts'),
    path('home/', CatalogHomeView.as_view(), name='home'),
]