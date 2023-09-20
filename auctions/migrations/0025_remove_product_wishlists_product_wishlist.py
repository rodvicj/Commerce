# Generated by Django 4.2.5 on 2023-09-20 16:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0024_remove_product_watchlist_product_wishlists"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="wishlists",
        ),
        migrations.AddField(
            model_name="product",
            name="wishlist",
            field=models.ManyToManyField(blank=True, related_name="wishlist", to=settings.AUTH_USER_MODEL),
        ),
    ]
