import os

from django import forms

from .models import Product, Category
from django.core.exceptions import ValidationError
from dotenv import load_dotenv


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'descriptions', 'category', 'price', 'img']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.update_field_attributes()

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

    def update_field_attributes(self):

        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Введите {self.fields[field_name].label.lower()}'
            })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        load_dotenv()
        lst_exception = os.getenv('LST_EXCEPTION')
        for lst in lst_exception:
            if lst in name.lower():
                raise ValidationError('Вы ввели запрещенное слово')
        return name

    def clean_descriptions(self):
        descriptions = self.cleaned_data.get('descriptions')
        load_dotenv()
        lst_exception = os.getenv('LST_EXCEPTION')
        for lst in lst_exception:
            if lst in descriptions.lower():
                raise ValidationError('Вы ввели запрещенное слово')
        return descriptions

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('Цена не может быть ниже нуля или равняться нулю')
        return price


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['description', 'name']



