from django.shortcuts import render
from .models import Commission

def commissions_list(request):
    commissions = Commission.objects.all()
    return render(request, "commission_content.html", {'commissions': commissions},)

def commissions_detail(request, pk):
    comments = Commission.objects.get(pk=pk).comments.all()
    return render(request, "commission_comments.html", {"comments": comments},)