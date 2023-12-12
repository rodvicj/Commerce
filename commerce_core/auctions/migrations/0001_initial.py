# Generated by Django 4.2.7 on 2023-11-29 03:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
                ("image", models.ImageField(null=True, upload_to="images/")),
                ("name", models.CharField(max_length=200)),
                ("price_amount", models.PositiveBigIntegerField()),
                ("quantity", models.PositiveBigIntegerField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
                (
                    "activation_status",
                    models.CharField(
                        choices=[("ACTIVE", "Active"), ("DRAFT", "Draft")],
                        default="DRAFT",
                        max_length=6,
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CartProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
                ("quantity", models.PositiveBigIntegerField()),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cart_products",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cart_products",
                        to="auctions.product",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="cartproduct",
            constraint=models.UniqueConstraint(fields=("buyer", "product"), name="unique_cart_product"),
        ),
    ]