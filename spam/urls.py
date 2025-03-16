from django.urls import path

from .views import (
    SpamCreateView,
    SpamDeleteView,
    SpamDetailView,
    SpamHomeView,
    SpamListView,
    SpamUpdateView,
)

app_name = "spam"


urlpatterns = [
    path("", SpamHomeView.as_view(), name="homes"),
    path("spam_list/", SpamListView.as_view(), name="spam_list"),
    path("spam_detail/<int:pk>/", SpamDetailView.as_view(), name="spam_detail"),
    path("create/", SpamCreateView.as_view(), name="create"),
    path("spam/<int:pk>/delete/", SpamDeleteView.as_view(), name="delete"),
    path("spam_detail/<int:pk>/update/", SpamUpdateView.as_view(), name="update"),
]
