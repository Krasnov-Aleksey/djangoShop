from django.core.management import BaseCommand
from shopapp.models import Order, Client, Product


class Command(BaseCommand):
    help = 'Create order'

    def handle(self, *args, **kwargs):
        client = Client.objects.get(id=18)
        order = Order(client=client, total_price=f'{10}')
        order.save()
        product = Product.objects.get(id=3)
        order.products.add(product)
        product = Product.objects.get(id=6)
        order.products.add(product)
        product = Product.objects.get(id=9)
        order.products.add(product)
