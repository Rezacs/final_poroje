# Generated by Django 3.2.9 on 2021-12-31 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grups', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='category',
            field=models.ManyToManyField(to='grups.Category'),
        ),
    ]
