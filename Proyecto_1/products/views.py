from django.shortcuts import render
from django.shortcuts import HttpResponse
from products.models import Products

def create_products(request):
    new_product = Products.objects.create(name = "Mirinda", price = 7.0, stock = False)
    print(new_product)
    return HttpResponse("Nuevo producto creado")

def list_products(request):
    all_products = Products.objects.all()
    context = {"products":all_products}
    return render (request, "list_of_products.html", context= context)