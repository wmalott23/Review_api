from tkinter import CASCADE
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)


class Review(models.Model):
    prod_num = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    verbage = models.CharField(max_length=255)

