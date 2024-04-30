from django.core.management import BaseCommand
from shopapp.models import Order, Client, Product
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Create order'

    def handle(self, *args, **kwargs):
        client_dict = {}
        today = datetime.now()
        before = today - timedelta(days=365)
        clients = Client.objects.all()
        for client in clients:
            flag = True
            orders = Order.objects.filter(client=client, data_order__range=(before, today))
            product_list = []
            for order in orders:
                if flag:
                    client_order = client.name_client
                    flag = False
                products = order.products.all()
                for product in products:
                    product_list.append(product.name_product)
            # client_dict[client_order]=set(product_list)
            client_dict[client_order] = product_list
        for key, value in client_dict.items():
            print(key)
            print(value)

