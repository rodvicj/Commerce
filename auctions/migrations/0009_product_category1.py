# Generated by Django 4.1.7 on 2023-07-31 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category1',
            field=models.CharField(
                choices=[('fasion', 'Fashion'), ('toys', 'Toys'), ('electronics', 'Electronics'), ('home', 'Home'),
                         ('others', 'Others')],
                max_length=128,
                null=True
            ),
        ),
    ]
