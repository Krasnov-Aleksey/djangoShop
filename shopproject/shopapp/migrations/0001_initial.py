# Generated by Django 5.0.4 on 2024-04-20 05:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_client', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('number_phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=100)),
                ('registration_date_client', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=100)),
                ('description_product', models.TextField()),
                ('price_product', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity_product', models.DecimalField(decimal_places=3, max_digits=8)),
                ('added_date_product', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('data_order', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopapp.client')),
                ('products', models.ManyToManyField(to='shopapp.product')),
            ],
        ),
    ]
