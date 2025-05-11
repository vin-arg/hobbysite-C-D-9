from django.shortcuts import render, redirect
from .models import Article, ArticleCategory
from .forms import ArticleForm, ArticleCategoryForm
from django.contrib.auth.decorators import login_required

def article_list(request):
    articles = Article.objects.all()
    details = ArticleCategory.objects.all()
    categories = ArticleCategory.objects.prefetch_related('art_cat').all()
    return render(request, 'article_list.html', {'articles': articles, 'detail': details, 'categories':categories})

@login_required
def article_detail(request, num=1):
    article = Article.objects.filter(pk=num).first() 
    return render(request, 'article_detail.html', {'article': article})

def article_create(request):
    
    if (request.method == "POST"):
        form = ArticleForm(request.POST)
        category_form = ArticleCategoryForm(request.POST)

        if category_form.is_valid():
            category_form.save()
            return redirect('article_list')
        elif form.is_valid():
            form.save()
            return redirect('article_list')
        
    form = ArticleForm()
    category_form = ArticleCategoryForm()

    return render(request, 'article_create.html', {'article_form': form, 'category_form': category_form},)
