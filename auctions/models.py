from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import datetime


class User(AbstractUser):
    pass


# class Category(models.Model):
#     name = models.CharField(blank=True, max_length=32)

#     def __str__(self):
#         return f"{self.name}"


class Product(models.Model):
    # Fashion, Toys, Electronics, Home, etc.
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
    category = models.CharField(max_length=128, null=True, choices=choices)
    amount = models.PositiveIntegerField(blank=False)
    active = models.BooleanField(default=True)
    description = models.CharField(blank=False, max_length=512)
    image_url = models.URLField(blank=True)
    # category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name="categoryListings")
    # TODO: change this add watchlist to add to cart and change watchlist html to View cart instead
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlists")
    # watchlist1 = models.OneToOneField(User, blank=True, related_name="watchlists")

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
    quantity = models.PositiveIntegerField(blank=False, default=1)
    # quantity = models.PositiveIntegerField(blank=False)
    product = models.ForeignKey(
        Product, null=True, on_delete=models.CASCADE, related_name="cart_products"
    )
    # date = models.DateTimeField(default=datetime.now, blank=True)
    # data = models.CharField(max_length=255)


# class CartProduct(CreatedModified):
#     buyer = models.ForeignKey('users.User', related_name='cart_products', on_delete=models.CASCADE)
#     product = models.ForeignKey('shop.Product', related_name='cart_products', on_delete=models.CASCADE)
#     quantity = models.PositiveBigIntegerField()
