# from django.contrib.auth.models import User
from django.db import models

from ..models.product import Product


class CartProduct(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    buyer = models.ForeignKey("users.User", related_name="cart_products", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="cart_products", on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()

    class Meta:
        constraints = [models.UniqueConstraint(fields=["buyer", "product"], name="unique_cart_product")]

    def __str__(self):
        return f"Cart Product ID: {self.pk} | Buyer: {self.buyer.username} | Product: {self.product.name}"
