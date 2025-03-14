from django.db import models
from django.urls import reverse
# Create your models here.

class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:ingredientDetail', args=[self.pk])
    
class Comment(models.Model):
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name="comment", null=True)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipeDetail', args=[self.pk])