from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20,null=False,unique=True)
    pub = models.CharField(max_length=20,null=False)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    market_price = models.DecimalField(max_digits=5,decimal_places=2)
