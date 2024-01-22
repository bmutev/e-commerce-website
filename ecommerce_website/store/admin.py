from django.contrib import admin

# Register your models here.
from .models import Category
# from .models import Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     pass