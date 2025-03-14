from django.shortcuts import render
from .models import Article, ArticleCategory

def article_list(request):
    articles = Article.objects.all()
    details = ArticleCategory.objects.all()
    categories = ArticleCategory.objects.prefetch_related('art_cat').all()
    return render(request, 'article_list.html', {'articles': articles, 'detail': details, 'categories':categories})

def article_detail(request, num=1):
    article = Article.objects.filter(pk=num).first() 
    return render(request, 'article_detail.html', {'article': article})
