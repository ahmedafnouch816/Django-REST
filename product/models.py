from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(max_length=250)
    prix = models.DecimalField(max_digits=5, decimal_places=2)