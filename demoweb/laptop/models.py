from django.db import models

# Create your models here.
class laptopModel(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    price = models.IntegerField()
    discount = models.FloatField()
    image = models.FileField()
    description = models.TextField()