from catalog.models import Product

from config.settings import CACHE_ENABLE

from django.core.cache import cache


class CategoryProduct:
    @staticmethod
    def category_product(category_id):
        return (
            Product.objects
            .filter(category_id=category_id)
            .select_related('category')
            .prefetch_related('images')
        )

    @staticmethod
    def get_products_from_cache():
        if not CACHE_ENABLE:
            return Product.objects.all()
        key = "product_list"
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products)
        return products

