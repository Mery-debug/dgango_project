from django.db.models.signals import post_save
from django.dispatch import receiver
from catalog.models import Product


@receiver(post_save, sender=Product)
def assign_permissions_to_owner(instance, created, **kwargs):
    if created:
        owner = instance.owner
        if owner:
            owner.user_permissions.add('authorization.can_edit_product')
