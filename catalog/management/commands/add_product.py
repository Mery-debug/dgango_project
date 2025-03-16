from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add new category or product to the database"

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            Category.objects.all().delete()
            Product.objects.all().delete()

            call_command("loaddata", settings.BASE_DIR / "category_fixture.json")
            call_command("loaddata", settings.BASE_DIR / "product_fixture.json")
