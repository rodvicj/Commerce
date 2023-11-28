from django.db import models


class Item(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to="images/", null=True)
    name = models.CharField(max_length=200)
    price_amount = models.PositiveBigIntegerField()
    quantity = models.PositiveBigIntegerField()

    class Meta:
        abstract = True
