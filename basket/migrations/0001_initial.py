# Generated by Django 3.2.9 on 2021-12-31 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('live', 'live_basket_now'), ('past', 'payed and cheked'), ('done', 'finished basket')], max_length=4)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True, help_text='Enter a description for your selected prod.')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('shipping_date', models.DateTimeField()),
                ('shippment', models.CharField(choices=[('pey', 'peyk_motori'), ('pos', 'post'), ('dgp', 'digikala_post')], max_length=3)),
                ('basket', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='basket.basket')),
            ],
        ),
        migrations.CreateModel(
            name='Email_response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True, help_text='Enter a description for your selected prod.')),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('seller_response', models.CharField(max_length=300)),
                ('buyer_response', models.CharField(max_length=300)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.order')),
            ],
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.basket')),
            ],
        ),
    ]