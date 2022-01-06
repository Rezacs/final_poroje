# Generated by Django 3.2.9 on 2022-01-06 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_shop_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('show', 'show this image'), ('dont', 'dont show this image')], max_length=4, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.products')),
            ],
        ),
    ]
