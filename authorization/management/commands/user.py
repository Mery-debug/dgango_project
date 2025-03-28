from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="m.a.shap58000@gmail.com")
        user.set_password("Qwerty1234%")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
