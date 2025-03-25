from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from config.settings import MODERATOR_GROUP


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

    @property
    def is_moderator(self) -> bool:
        return self.groups.filter(name=MODERATOR_GROUP).exists()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['email']


