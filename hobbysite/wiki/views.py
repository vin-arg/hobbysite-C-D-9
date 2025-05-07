from django.shortcuts import render, get_object_or_404
from .models import Article, ArticleCategory

def article_list_view(request):
    articles = Article.objects.all()
    articlecategories = ArticleCategory.objects.all()
    return render(request, "wiki/article_list.html", {
        "articles": articles,
        "articlecategories": articlecategories
    })

def article_detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "wiki/article_detail.html", {
        "article": article
    })