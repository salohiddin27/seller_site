from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=222)
    photo = models.ImageField(upload_to='categories/')

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


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity})"
