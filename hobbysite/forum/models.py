from django.db import models

# Create your models here.

class PostCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    #sort by name
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Post Categories"
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(PostCategory, null=True, blank=True, on_delete=models.SET_NULL)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    #sort by date
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title