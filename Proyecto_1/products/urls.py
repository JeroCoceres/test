from django.urls import path
from products.views import list_products, create_products, create_orders, list_orders

urlpatterns = [
    path("lista-de-productos/",list_products),
    path("crear-producto/", create_products),
    path("crear-orden/", create_orders),
    path("lista-de-ordenes/",list_orders),
]