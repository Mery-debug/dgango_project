from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Auth


class AuthForm(UserCreationForm):
    username = forms.CharField(max_length=15, required=False, help_text='Имя пользователя')
    email = forms.EmailField(required=True, help_text='Адрес почты')
    img = forms.ImageField(required=False, help_text='Изображение')
    country = forms.CharField(required=False, help_text='Страна')
    phone_number = forms.IntegerField(required=False, help_text='Номер должен содержать только цифры')

    class Meta:
        model = Auth
        fields = '__all__'

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры')
        return phone_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@%s.%s'):
            raise forms.ValidationError('Почта должна быть вида user@example.ru')
        return email





