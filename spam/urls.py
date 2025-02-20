from django.contrib import admin
from django.urls import path
from .views import CatalogContactsView, CatalogHomeView, CatalogCreateView, CatalogDeleteView, CatalogUpdateView, \
    CatalogViewDetail, CatalogViewList

app_name = 'catalog'


urlpatterns = [
    path("admin/", admin.site.urls),

]