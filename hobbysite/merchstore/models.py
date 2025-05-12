from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('product_type', args=[str(self.id)])


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, related_name="products", null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100)
    stock = models.IntegerField(default=0)

    status_choices = {
        "AVA": "Available",
        "SAL": "On Sale",
        "OUT": "Out of Stock",
    }
    status = models.CharField(choices=status_choices, default="AVA", max_length=3)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('product', args=[str(self.id)])
    

class Transaction(models.Model):
    buyer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField(default=0)

    status_choices = {
        "CAR": "On Cart",
        "PAY": "To Pay",
        "SHI": "To Ship",
        "REC": "To Receive",
        "DEL": "Delivered",
    }
    status = models.CharField(choices=status_choices, max_length=3, default="CAR")

    created_on = models.DateTimeField(auto_now_add=True)
