from django.db import models

# Create your models here.
class Bestseller(models.Model):
    id = models.BigIntegerField(primary_key = True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    flag = models.CharField(max_length=10)
    url = models.TextField()
    image = models.TextField()
    date = models.DateField(auto_now=True)
