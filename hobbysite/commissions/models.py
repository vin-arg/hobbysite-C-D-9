from django.db import models
from django.urls import reverse

class Commission(models.Model):
    
    STATUS_CHOICES=[
        ('Open', 'Open'),
        ('Full', 'Full'),
        ('Completed', 'Completed'),
        ('Discontinued', 'Discontinued'),
    ]
           
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="Open")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('commissions:commissions_detail', args=[self.pk])
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created_on']
    
class Job(models.Model):
    
    STATUS_CHOICES=[
        ('Open', 'Open'),
        ('Full', 'Full'),
    ]
    
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='Job', null=True)
    role = models.CharField(max_length=255)
    manpower_required = models.IntegerField()
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default="Open")
    
    class Meta:
        ordering = ['status']
        
class JobApplication(models.Model):
    
    STATUS_CHOICES=[
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='JobApplication', null=True)
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='JobApplication', null=True)
    status = models.CharField(max_length=255)
    applied_on = models.DateTimeField(auto_now_add=True)