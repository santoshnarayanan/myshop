from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # url for order create view
    path('create/', views.order_create, name='order_create'),
]