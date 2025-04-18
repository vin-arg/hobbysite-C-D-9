from django.shortcuts import render, redirect
from .models import Article, ArticleCategory
from .forms import ArticleForm, ArticleCategoryForm

def article_list(request):
    articles = Article.objects.all()
    details = ArticleCategory.objects.all()
    categories = ArticleCategory.objects.prefetch_related('art_cat').all()
    return render(request, 'article_list.html', {'articles': articles, 'detail': details, 'categories':categories})

def article_detail(request, num=1):
    article = Article.objects.filter(pk=num).first() 
    return render(request, 'article_detail.html', {'article': article})

def article_create(request):
    
    if (request.method == "POST"):
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('article_list')
        
    form = ArticleForm()

    return render(request, 'article_create.html', {'article_form': form},)
