from django.contrib import admin
from .models import *

class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id', 'name', 'product_type', 'price']

admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)