from django.db import models


# Create your models here.

class Stock(models.Model):
    symbol = models.CharField(max_length=500,unique=True)
    company_name = models.CharField(max_length=500)
    market_cap = models.FloatField()
