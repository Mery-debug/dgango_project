from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

import catalog


class Command(BaseCommand):
    help = 'Создание группы модератор продуктов'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Moder')

        can_unpublish_product = Permission.objects.get(
            codename='can_unpublish_product',
            content_type__app_label='catalog',
            content_type__model='product'
        )

        delete_product = Permission.objects.get(
            codename='delete_product',
            content_type__app_label='catalog',
            content_type__model='product'
        )

        group.permissions.add(can_unpublish_product, delete_product)