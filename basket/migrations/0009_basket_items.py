# Generated by Django 3.2.9 on 2022-01-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_shop_type'),
        ('basket', '0008_alter_basketitem_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='items',
            field=models.ManyToManyField(through='basket.BasketItem', to='products.Products'),
        ),
    ]