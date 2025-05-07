from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ArticleForm
from .models import Article, ArticleCategory

@login_required
def article_create_view(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return HttpResponseRedirect(reverse("wiki:article_detail", args=[article.pk]))
    else:
        form = ArticleForm()
    return render(request, "wiki/article_form.html", {"form": form})


@login_required
def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if article.author != request.user:
        return redirect("wiki:articles")

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("wiki:article_detail", pk=article.pk)
    else:
        form = ArticleForm(instance=article)

    return render(request, "wiki/article_form.html", {"form": form})

def article_list_view(request):
    articles = Article.objects.all()
    articlecategories = ArticleCategory.objects.prefetch_related('articles').all()
    return render(request, "wiki/article_list.html", {
        "articles": articles,
        "articlecategories": articlecategories
    })

def article_detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "wiki/article_detail.html", {"article": article})