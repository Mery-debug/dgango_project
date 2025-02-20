from django.contrib import admin
from .models import Spam


@admin.register(Spam)
class SpamAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
    list_filter = ('name',)
    search_fields = ('name',)

