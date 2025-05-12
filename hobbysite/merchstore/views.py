from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def item_list(request):
    products = Product.objects.all()
    product_types = ProductType.objects.all()
    return render(request, "item_list.html", {'products': products, 'product_types': product_types})

@login_required
def item_entry(request, num=1):

    product = Product.objects.get(id=num)
    product_type = product.product_type
    return render(request, "item_entry.html", {'product': product, 'product_type': product_type})

@login_required
def item_add(request):
    form = ProductAddForm()
    if request.method == 'POST':
        form = ProductAddForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user.profile
            product.save()
            return redirect('item_list')
    return render(request, "item_add.html", {'add_form': form})