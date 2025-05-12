from django import forms
from .models import *

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["amount",]

class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'description', 'price', 'stock',]
    
class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'description', 'price', 'stock',]

