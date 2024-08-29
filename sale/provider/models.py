from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    active = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    provider = models.ForeignKey(Provider , on_delete=models.PROTECT , )
    def __str__(self) -> str:
        return self.name
# Create your models here.
