from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Client, Order, Product
from .forms import ProductForm, UploadPhoto
from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage


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


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product_selection = form.cleaned_data['product_selection']
            description_product = form.cleaned_data['description_product']
            price_product = form.cleaned_data['price_product']
            quantity_product = form.cleaned_data['quantity_product']
            added_date_product = form.cleaned_data['added_date_product']
            select_product = Product.objects.get(name_product=product_selection.name_product)
            select_product.description_product = description_product
            select_product.price_product = price_product
            select_product.quantity_product = quantity_product
            select_product.added_date_product = added_date_product
            select_product.save()
    else:
        form = ProductForm()

    return render(request, 'shopapp/product_form.html', {'form': form})


def upload_photo(request):
    if request.method == 'POST':
        form = UploadPhoto(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['photo']
            fs = FileSystemStorage()
            fs.save(photo.name, photo)
    else:
        form = UploadPhoto()
    return render(request, 'shopapp/upload_photo.html', {'form': form})
