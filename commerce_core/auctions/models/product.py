from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .item import Item


class ActivationStatus(models.TextChoices):
    ACTIVE = "ACTIVE", _("Active")
    DRAFT = "DRAFT", _("Draft")


class Product(Item):  # type: ignore
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    activation_status = models.CharField(
        choices=ActivationStatus.choices, max_length=6, default=ActivationStatus.DRAFT
    )
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"Product ID: {self.pk} | " f"Name: {self.name} | " f"Price: {self.price_amount}")
