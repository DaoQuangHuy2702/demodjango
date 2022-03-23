from django.db import models

# Create your models here.

class bookModel(models.Model):
    title = models.CharField(max_length=100)
    barcode = models.CharField(max_length=50)
    coverType = models.CharField(max_length=30)
    price = models.IntegerField()
    discount = models.FloatField()
    image = models.FileField()
    description = models.TextField()
