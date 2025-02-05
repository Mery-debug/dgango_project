from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.db import transaction


class Command(BaseCommand):
    help = 'Add new category or product to the database'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            Category.objects.all().delete()
            Product.objects.all().delete()

            category, _ = Category.objects.get_or_create(name='category1')

            products = [
                {'name': 'product123', 'descriptions': 'description test edition1', 'category': category, 'price': 1500},
                {'name': 'product234', 'descriptions': 'description test edition2', 'category': category, 'price': 500},
                {'name': 'product345', 'descriptions': 'description test edition3', 'category': category, 'price': 100},
            ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name} {product.price}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name} {product.price}'))