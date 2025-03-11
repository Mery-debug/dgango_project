from django.contrib import admin
from django.urls import path
from .views import AuthRegister, AuthHome
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'authorization'


urlpatterns = [
    path("admin/", admin.site.urls),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('login/', LoginView.as_view(template_name='templates/login.html'), name='login'),
    path('register/', AuthRegister.as_view(), name='register'),
    path('home/', AuthHome.as_view(), name='home'),
]