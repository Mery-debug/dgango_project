from django.db import models


class Category(models.Model):
    description = models.TextField(max_length=500, verbose_name='описание')
    name = models.CharField(max_length=150, verbose_name='наименование')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    descriptions = models.TextField(max_length=500, verbose_name='описание')
    img = models.ImageField(upload_to='images/', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(verbose_name='цена')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.img} {self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

