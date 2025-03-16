import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Auth

# from django.core.validators import EmailValidator


class AuthForm(UserCreationForm):
    username = forms.CharField(
        max_length=15, required=False, help_text="Имя пользователя"
    )
    email = forms.EmailField(required=True, help_text="Адрес почты")
    img = forms.ImageField(required=False, help_text="Изображение")
    country = forms.CharField(required=False, help_text="Страна")
    phone_number = forms.CharField(
        required=False, help_text="Номер должен содержать только цифры"
    )

    class Meta:
        model = Auth
        fields = ["email", "password1", "password2"]

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_pattern, email):
            raise forms.ValidationError("Почта должна быть вида user@example.ru")
        return email

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if Auth.objects.filter(username=username).exists():
            raise ValidationError(f"Пользователь с именем {username} уже существует.")

        elif Auth.objects.filter(email=email).exists():
            raise ValidationError(f"Пользователь с почтой {email} уже существует.")
