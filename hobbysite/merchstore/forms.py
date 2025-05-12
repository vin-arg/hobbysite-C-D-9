from django import forms
from .models import *

class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'description', 'price', 'stock',]

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'description', 'price', 'stock',]