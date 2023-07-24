from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import datetime


class User(AbstractUser):
    pass


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    amount = models.PositiveIntegerField(blank=False, null=True)

    def __str__(self):
        return f"${self.amount}"


class Category(models.Model):
    name = models.CharField(blank=True, max_length=32)

    def __str__(self):
        return f"{self.name}"


class Listing(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="lists")
    title = models.CharField(blank=False, max_length=128)
    starting_bid = models.PositiveIntegerField(blank=False)
    current_bid = models.ForeignKey(Bid, null=True, blank=True, on_delete=models.CASCADE, related_name="item_list")
    active = models.BooleanField(default=True)
    description = models.CharField(blank=False, max_length=512)
    image_url = models.URLField(blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name="categoryListings")
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlists")

    def __str__(self):
        return f"{self.title} - {self.user}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    list = models.ForeignKey(Listing, null=True, on_delete=models.CASCADE, related_name="comments")
    date = models.DateTimeField(default=datetime.now, blank=True)
    data = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} commented {self.data} in {self.list.title}"

