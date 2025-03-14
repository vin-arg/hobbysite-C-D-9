from django.shortcuts import render
from .models import Comment, Commission

def commissions_list(request):
    commissions = Commission.objects.all()
    return render(request, "commission_content.html", {'commissions': commissions},)

def commissions_detail(request, pk):
    details = Comment.objects.get(pk=pk)
    return render(request, "commission_comments.html", {"details": details},)