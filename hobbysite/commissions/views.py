from django.shortcuts import render
from .models import Commission

def commissions_list(request):
    commissions = Commission.objects.all()
    ctx = {
        'commissions': commissions
    }
    return render(request, 'commission_content.html', ctx,)

def commissions_detail(request, pk):
    commission_info = Commission.objects.get(pk=pk)
    ctx = {
        'comments': commission_info.comments.all(),
        'commission': commission_info
    }
    return render(request, 'commission_comments.html', ctx,)