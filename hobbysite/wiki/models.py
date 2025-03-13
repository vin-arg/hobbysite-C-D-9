from django.db import models
from django.urls import reverse

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null = True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, on_delete = models.SET_NULL, null = True, related_name = "articles")
    entry = models.TextField(null = True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title