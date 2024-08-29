from django.db import models
from provider.models import Provider , Product
class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    wallet = models.FloatField(default= 0 )
    def __str__(self) -> str:
        return self.name
    
class Sale(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)