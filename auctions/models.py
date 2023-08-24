from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Product(models.Model):
    choices = (
        ("fashion", "Fashion"),
        ("toys", "Toys"),
        ("electronics", "Electronics"),
        ("home", "Home"),
        ("others", "Others"),
    )
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="lists")
    title = models.CharField(blank=False, max_length=128)
    date = models.DateTimeField(default=datetime.now, blank=True)
    quantity = models.PositiveIntegerField(blank=False, default=1)
    category = models.CharField(max_length=128, null=True, choices=choices)
    amount = models.PositiveIntegerField(blank=False)
    active = models.BooleanField(default=True)
    description = models.CharField(blank=False, max_length=512)
    image_url = models.URLField(blank=True)
    # TODO: change this add watchlist to add to cart and change watchlist html
    # to View cart instead;
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlists")

    def __str__(self):
        return f"{self.title} - {self.user}"


class Cart(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_products")
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name="cart_products")
    quantity = models.PositiveIntegerField(default=1)
