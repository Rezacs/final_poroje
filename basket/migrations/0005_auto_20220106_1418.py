# Generated by Django 3.2.9 on 2022-01-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0004_basketitem_chekedout_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketitem',
            name='Chekedout_date',
        ),
        migrations.AddField(
            model_name='basket',
            name='Chekedout_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]