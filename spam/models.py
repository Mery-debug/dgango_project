from django.db import models


class Spam(models.Model):
    name = models.CharField(max_length=100, verbose_name='заголовок')
    content = models.TextField(max_length=1500, verbose_name='содержимое')
    img = models.ImageField(upload_to='media/img/', default='404 error', verbose_name='изображение')
    view_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.content}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['name']
