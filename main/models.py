from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=20)
    year = models.CharField(max_length=10)
    amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    description = models.TextField()
    Class = models.CharField(max_length=10)
    developer_name = models.CharField(max_length=30)
    app_name = models.CharField(max_length=30)
    

