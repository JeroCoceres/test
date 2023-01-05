from django.shortcuts import render
from django.shortcuts import HttpResponse
from products.models import Products, Orders

def create_products(request):
    new_product = Products.objects.create(name = "Mirinda", price = 7.0, stock = False)
    print(new_product)
    return HttpResponse("Nuevo producto creado")

def list_products(request):
    all_products = Products.objects.all()
    context = {"products":all_products}
    return render (request, "list_of_products.html", context= context)

def create_orders(request):
    new_order = Orders.objects.create(name = "Pedro", payment = "Card")
    return HttpResponse("Nueva orden creada")

def list_orders(request):
    all_orders = Orders.objects.all()
    context = {"orders":all_orders}
    return render (request, "list_of_orders.html", context= context)