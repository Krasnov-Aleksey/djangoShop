from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Client, Order
from datetime import datetime, timedelta


def index(request):
    return render(request, 'shopapp/index.html')


def client_all(request):
    clients = Client.objects.all()
    return render(request, 'shopapp/client_all.html', {'clients': clients})


def client_order_id(request, client_id):
    order_dict = {}
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client).all()
    for order in orders:
        products = order.products.all()
        product_list = []
        for product in products:
            product_list.append(product)
        order_dict[order] = product_list
    return render(request, 'shopapp/client_order_id.html', {'client': client,
                                                            'order_dict': order_dict})


def date_7(request, date=7):
    title = f'Заказы за последние {date} дней'
    client_dict = {}
    today = datetime.now()
    before = today - timedelta(days=date)
    clients = Client.objects.all()
    for client in clients:
        orders = Order.objects.filter(client=client, data_order__range=(before, today))
        product_list = []
        for order in orders:
            products = order.products.all()
            for product in products:
                product_list.append(product.name_product)
        client_dict[client] = set(product_list)
    return render(request, 'shopapp/date_7.html', {'title': title, 'client_dict': client_dict})


def date_30(request, date=30):
    title = f'Заказы за последние {date} дней'
    client_dict = {}
    today = datetime.now()
    before = today - timedelta(days=date)
    clients = Client.objects.all()
    for client in clients:
        orders = Order.objects.filter(client=client, data_order__range=(before, today))
        product_list = []
        for order in orders:
            products = order.products.all()
            for product in products:
                product_list.append(product.name_product)
        client_dict[client] = set(product_list)
    return render(request, 'shopapp/date_7.html', {'title': title, 'client_dict': client_dict})


def date_365(request, date=365):
    title = f'Заказы за последние {date} дней'
    client_dict = {}
    today = datetime.now()
    before = today - timedelta(days=date)
    clients = Client.objects.all()
    for client in clients:
        orders = Order.objects.filter(client=client, data_order__range=(before, today))
        product_list = []
        for order in orders:
            products = order.products.all()
            for product in products:
                product_list.append(product.name_product)
        client_dict[client] = set(product_list)
    return render(request, 'shopapp/date_7.html', {'title': title, 'client_dict': client_dict})
