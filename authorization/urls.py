from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from catalog.views import (
    CatalogCreateView,
    CatalogDeleteView,
    CatalogUpdateView,
    CatalogViewDetail,
    CatalogViewList, CategoryView,
)
from spam.views import (
    SpamCreateView,
    SpamDeleteView,
    SpamDetailView,
    SpamListView,
    SpamUpdateView,
)

from .views import AuthHome, AuthRegister, CustomLogoutView

app_name = "authorization"


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "logout/", LogoutView.as_view(next_page="authorization:goodbye"), name="logout"
    ),
    path(
        "goodbye/",
        CustomLogoutView.as_view(template_name="authorization/goodbye.html"),
        name="goodbye",
    ),
    path(
        "login/",
        LoginView.as_view(
            template_name="authorization/login.html", next_page="authorization:home"
        ),
        name="login",
    ),
    path(
        "register/",
        AuthRegister.as_view(template_name="authorization/register.html"),
        name="register",
    ),
    path(
        "product_list/",
        CatalogViewList.as_view(template_name="authorization/products.html"),
        name="product_list",
    ),
    path(
        "product_detail/<int:pk>/",
        CatalogViewDetail.as_view(template_name="authorization/product.html"),
        name="product_detail",
    ),
    path(
        "product/new/",
        CatalogCreateView.as_view(template_name="authorization/create_product.html"),
        name="product_create",
    ),
    path(
        "product/<int:pk>/edit/",
        CatalogUpdateView.as_view(template_name="authorization/update_product.html"),
        name="product_edit",
    ),
    path(
        "product/<int:pk>/delete/",
        CatalogDeleteView.as_view(template_name="catalog/confirm_delete.html"),
        name="product_delete",
    ),
    path(
        "spam_detail/<int:pk>/update/",
        SpamUpdateView.as_view(template_name="authorization/update_spam.html"),
        name="update",
    ),
    path(
        "spam_list/",
        SpamListView.as_view(template_name="authorization/contents.html"),
        name="spam_list",
    ),
    path(
        "spam_detail/<int:pk>/",
        SpamDetailView.as_view(template_name="authorization/content.html"),
        name="spam_detail",
    ),
    path(
        "create/",
        SpamCreateView.as_view(template_name="authorization/create_spam.html"),
        name="create_spam",
    ),
    path(
        "spam/<int:pk>/delete/",
        SpamDeleteView.as_view(template_name="authorization/confirm_delete.html"),
        name="delete_spam",
    ),
    path(
        "authorization/category_list/<str:pk>",
        CategoryView.as_view(template_name="authorization/category.html"),
        name="category_list",
    ),
    path("", AuthHome.as_view(), name="home"),
]
