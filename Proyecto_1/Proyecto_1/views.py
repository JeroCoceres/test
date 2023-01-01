from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def hola(request):
    return HttpResponse("Hola muñeco, que haces bebe")

def fecha_actual(request):
    today = datetime.now().date()
    return HttpResponse(f"la fecha de hoy es {today}")

def indice(request):
    return render(request, "index.html", context={})

def vista_con_template(request):
    return render(request, "template.html", context= {})

def saludo_desde_template(request):
    nombre = "Jero"
    edad = 25
    context = {
        "nombre" : nombre, 
        "edad" : edad,
        "Usa lentes" : True,
        "lista" : [1,2,3,4,5]  
    }
    return render(request, "saludo.html", context=context)    