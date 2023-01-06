from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField( max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2500)
    
class discount(models.Model):
    code = models.CharField( max_length=50)
    description = models.CharField(max_length=250)
    discount = models.FloatField()