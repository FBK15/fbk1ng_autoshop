from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=30, default="")
    year = models.CharField(max_length=10)
    amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Developer(models.Model):
    username = models.CharField(max_length=20, null=True)
    user_class = models.CharField(max_length=20)
    
    

    
    

