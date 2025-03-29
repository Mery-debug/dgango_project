from catalog.models import Product


class CategoryProduct:
    @staticmethod
    def category_product(category_id):
        product = Product.objects.filter(category_id=category_id)
        if not product.exists():
            return []
        return product

