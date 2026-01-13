from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=222)
    photo = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=222)
    price = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='products/')
    brand = models.CharField(max_length=222)
    reviews = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return (f"{self.name} {self.price} {self.description}"
                f"{self.photo} {self.brand} {self.reviews}")

