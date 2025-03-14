from django.db import models
from django.urls import reverse

class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('commissions:commissions_detail', args=[self.pk])
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created_on']
    
class Comment(models.Model):
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='comments', null=True)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_on']