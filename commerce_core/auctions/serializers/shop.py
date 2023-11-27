# from datetime import datetime

# # from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
# from django.db import models
# from django.utils.translation import gettext_lazy as _

# # class User(AbstractUser):
# #     pass

# class Category(models.TextChoices):
#     FASHION = "FASHION", _("Fashion")
#     TOYS = "TOYS", _("Toys")
#     ELECTRONICS = "ELECTRONICS", _("Electronics")
#     HOME = "HOME", _("Home")
#     OTHERS = "OTHERS", _("Others")

# class Product(models.Model):
#     active = models.BooleanField(default=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lists")
#     title = models.CharField(max_length=128)
#     date = models.DateTimeField(default=datetime.now)
#     quantity = models.PositiveIntegerField(default=1)
#     category = models.CharField(choices=Category.choices, max_length=11)
#     amount = models.PositiveIntegerField()
#     description = models.CharField(max_length=512)
#     image_url = models.URLField()
#     wishlists = models.ManyToManyField(User, blank=True, related_name="wishlists")

#     def __str__(self):
#         return f"{self.title} - {self.user}"

# class Cart(models.Model):
#     buyer = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="cart_products"
#     )
#     product = models.ForeignKey(
#         Product, on_delete=models.CASCADE, related_name="cart_products"
#     )
#     quantity = models.PositiveIntegerField(default=1)
