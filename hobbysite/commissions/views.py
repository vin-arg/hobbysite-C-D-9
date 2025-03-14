from django.shortcuts import render
from .models import Commission

def commissions_list(request):
    commissions = Commission.objects.all()
    return render(request, 'commission_content.html', {'commissions': commissions},)

def commissions_detail(request, pk):
    commission_info = Commission.objects.get(pk=pk)
    return render(request, 'commission_comments.html', {'comments': commission_info.comments.all(), 'commission': commission_info},)