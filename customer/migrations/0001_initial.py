# Generated by Django 3.2.9 on 2021-12-31 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=300, null=True)),
                ('last_name', models.CharField(blank=True, max_length=300, null=True)),
                ('user_name', models.CharField(max_length=100, unique=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('phone', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('gender', models.CharField(blank=True, choices=[('mal', 'male'), ('fem', 'female'), ('not', 'notset')], max_length=3, null=True)),
                ('theme', models.CharField(blank=True, choices=[('gre', 'green'), ('pur', 'purpule'), ('red', 'red'), ('blu', 'blue')], max_length=3, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['user_name'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
            options={
                'ordering': ['customer'],
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('street', models.CharField(blank=True, max_length=150, null=True)),
                ('alley', models.CharField(blank=True, max_length=150, null=True)),
                ('number', models.CharField(blank=True, max_length=150, null=True)),
                ('zip', models.CharField(max_length=150)),
                ('desc', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]