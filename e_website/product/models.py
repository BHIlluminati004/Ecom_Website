from django.db import models

# Create your models here.
class Product(models.Model):
    Name=models.CharField(max_length=100)
    Description=models.TextField()
    Price=models.IntegerField()

class Image(models.Model):
    Wildphotography=models.CharField(max_length=500)
        
        
