from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Auth(AbstractUser):
    username = models.CharField(blank=True, null=True, verbose_name="Имя пользователя")
    email = models.EmailField(unique=True, verbose_name="Адрес почты")
    img = models.ImageField(
        upload_to="media/img/", blank=True, null=True, verbose_name="Изображение"
    )
    country = models.CharField(null=True, blank=True, verbose_name="Страна")
    phone_number = models.IntegerField(
        null=True, blank=True, help_text="Номер должен содержать только цифры"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        self.is_active = True
        return reverse("authorization:home")

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['email']
        permissions = [
            ("can_unpublish_product", "can unpublish new product"),
            ("can_delete_product", "can delete product"),
            ("can_edit_product", "can edit product"),
            ("can_add_product", "can add product")
        ]


