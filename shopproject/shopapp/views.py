from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return render(response, 'shopapp/index.html')


def client_all(response):
    return render(response, 'shopapp/client_all.html')
