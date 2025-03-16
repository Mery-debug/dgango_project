from django.db import models


class Category(models.Model):
    description = models.TextField(max_length=500, verbose_name="описание")
    name = models.CharField(max_length=150, verbose_name="наименование")

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, verbose_name="наименование")
    descriptions = models.TextField(max_length=500, verbose_name="описание")
    img = models.ImageField(
        upload_to="media/img/", default="404 error", verbose_name="изображение"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    price = models.DecimalField(decimal_places=10, max_digits=14, verbose_name="цена")
    view_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name"]
