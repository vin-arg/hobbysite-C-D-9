from django import forms
from .models import Article, ArticleCategory


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'category', 'entry']

class ArticleCategoryForm(forms.ModelForm):
    class Meta:
        model = ArticleCategory
        fields = '__all__'
