from django.shortcuts import render

def article_list(request):
    return render(request)

def article_detail(request, num=1):
    return render(request)
