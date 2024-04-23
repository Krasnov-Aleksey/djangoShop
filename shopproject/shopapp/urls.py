from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client_all/', views.client_all, name='client_all')
]