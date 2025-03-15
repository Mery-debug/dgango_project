from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authorization import views
from authorization.views import AuthHome

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalog/", include('catalog.urls', namespace='catalog')),
    path("spam/", include('spam.urls', namespace='spam')),
    path("authorization/", include('authorization.urls', namespace='authorization')),
    path("", AuthHome.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
