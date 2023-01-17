from django.db import models

# Create your models here.
class Gundam(models.Model):
    name = models.CharField(max_length=1000)
    price = models.IntegerField()
    shippingCost = models.IntegerField()
    shippingDate = models.CharField(max_length=100)
    image = models.CharField(max_length=2000)