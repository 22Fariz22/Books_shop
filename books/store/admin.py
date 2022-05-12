from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.
from store.models import Book


@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass