# Generated by Django 4.2.4 on 2023-08-19 03:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0022_alter_cart_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="date",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="cart",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
    ]