from django.shortcuts import render
from .models import *

def item_list(request):
    products = Product.objects.all()
    product_types = ProductType.objects.all()
    return render(request, "item_list.html", {'products': products, 'product_types': product_types})

def item_entry(request, num=1):

    product = Product.objects.get(id=num)
    product_type = product.product_type
    return render(request, "item_entry.html", {'product': product, 'product_type': product_type})