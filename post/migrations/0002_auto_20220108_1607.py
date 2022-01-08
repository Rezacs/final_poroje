# Generated by Django 3.2.9 on 2022-01-08 16:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('writer', 'title')},
        ),
    ]
