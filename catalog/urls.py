from django.urls import path

from .views import CatalogContactsView, CatalogHomeView

app_name = "catalog"


urlpatterns = [
    path("contacts/", CatalogContactsView.as_view(), name="contacts"),
    path("home/", CatalogHomeView.as_view(), name="homel"),
]
