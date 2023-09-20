# Generated by Django 4.2.5 on 2023-09-20 16:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0025_remove_product_wishlists_product_wishlist"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="wishlist",
        ),
        migrations.AddField(
            model_name="product",
            name="wishlists",
            field=models.ManyToManyField(blank=True, related_name="wishlists", to=settings.AUTH_USER_MODEL),
        ),
    ]