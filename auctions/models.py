from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

# from django.db.models.expressions import fields
# from django.db.models.fields import validators
# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.forms import fields_for_model


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
    user = models.ForeignKey(
        User, blank=False, on_delete=models.CASCADE, related_name="lists"
    )
    title = models.CharField(blank=False, max_length=128)
    quantity = models.PositiveIntegerField(blank=False, default=1)
    category = models.CharField(max_length=128, null=True, choices=choices)
    amount = models.PositiveIntegerField(blank=False)
    active = models.BooleanField(default=True)
    description = models.CharField(blank=False, max_length=512)
    image_url = models.URLField(blank=True)
    # TODO: change this add watchlist to add to cart and change watchlist html to View cart instead
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlists")

    def __str__(self):
        return f"{self.title} - {self.user}"


# TODO: change this comment to Cart
class Comment(models.Model):
    user = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="comments"
    )
    list = models.ForeignKey(
        Product, null=True, on_delete=models.CASCADE, related_name="comments"
    )
    date = models.DateTimeField(default=datetime.now, blank=True)
    data = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} commented {self.data} in {self.list.title}"


class Cart(models.Model):
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cart_products"
    )
    product = models.ForeignKey(
        Product, null=True, on_delete=models.CASCADE, related_name="cart_products"
    )
    quantity = models.PositiveIntegerField(default=1)
