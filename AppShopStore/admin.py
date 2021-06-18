from django.contrib import admin
from .models import Product, Category


# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'old_price', 'image_tag']


admin.site.register(Product, AdminProduct)


class AdminCategory(admin.ModelAdmin):
    list_display = ['title', 'created']


admin.site.register(Category, AdminCategory)
