from django.contrib import admin
from .models import ArticleCategory, Article

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_on', 'updated_on',)
    search_fields = ('title', 'entry',)
    list_filter = ('category', 'created_on',)

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
