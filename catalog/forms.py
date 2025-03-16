import os

from django import forms
from django.core.exceptions import ValidationError
from dotenv import load_dotenv

from .models import Product

load_dotenv()


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.update_field_attributes()
        self.lst_exception = os.getenv("LST_EXCEPTION").split(",")

    class Meta:
        model = Product
        fields = ["name", "descriptions", "category", "price", "img"]

    def update_field_attributes(self):
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update(
                {
                    "class": "form-control",
                    "placeholder": f"Введите {self.fields[field_name].label.lower()}",
                }
            )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        for lst in self.lst_exception:
            if lst.strip().lower() in name.lower():
                raise ValidationError("Вы ввели запрещенное слово")
        return name

    def clean_descriptions(self):
        descriptions = self.cleaned_data.get("descriptions")
        for lst in self.lst_exception:
            if lst.strip().lower() in descriptions.lower():
                raise ValidationError("Вы ввели запрещенное слово")
        return descriptions

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price <= 0:  # Проверка на None
            raise ValidationError("Цена не может быть ниже нуля или равняться нулю")
        return price

    def clean_img(self):
        img = self.cleaned_data.get("img")
        if img:
            return img
        else:
            img_name = img.name.lower()
            if not (
                img_name.endswith(".jpeg")
                or img_name.endswith(".png")
                or img_name.endswith(".jpg")
            ):
                raise ValidationError(
                    "Выберите изображение в формате .jpeg, .jpg или .png"
                )
            max_size = 5 * 1024 * 1024
            if img.size > max_size:
                raise ValidationError(
                    "Максимальный вес загружаемого изображения не должен превышать 5 Мб "
                )
            return img
