from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class ArticleCategory(models.Model):
    """Model representing an article category."""
    
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Article(models.Model):
    """Model representing an article."""
    
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ArticleCategory, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="articles"
    )
    entry = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles", default=1)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} by {self.author.username}"