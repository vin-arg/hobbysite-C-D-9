from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import *

def commissions_list(request):
    commissions = Commission.objects.all()
    return render(request, "commission_list.html", {'commissions': commissions})

def commissions_detail(request, num=1):
    details = Comment.objects.get(id=num)
    return render(request, "commission_detail.html", {"details": details})