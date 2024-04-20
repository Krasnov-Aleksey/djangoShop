from django.db import models


class Client(models.Model):
    name_client = models.CharField(max_length=30)
    email = models.EmailField()
    number_phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    registration_date_client = models.DateField()


class Product(models.Model):
    name_product = models.CharField(max_length=100)
    description_product = models.TextField()
    price_product = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_product = models.DecimalField(decimal_places=3)
    added_date_product = models.DateField()


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(decimal_places=2)
    data_order = models.DateTimeField(auto_now_add=True)
