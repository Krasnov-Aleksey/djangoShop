from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('client_all/', views.client_all, name='client_all'),
    path('client_order/<int:client_id>/', views.client_order_id, name='client_order_id'),
    path('data_7/', views.date_7, name='date_7'),
    path('data_30/', views.date_30, name='date_30'),
    path('data_365/', views.date_365, name='date_365'),
    path('product_form/', views.product_form, name='product_form'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),
]
