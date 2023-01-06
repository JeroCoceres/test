from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name= "Nombre")
    price = models.FloatField(verbose_name="Precio")
    stock = models.BooleanField(verbose_name="Stock")


    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Orders(models.Model):
    CHOICES = (
        ("Card","Card"),
        ("Cash","Cash"),
    )
    name = models.CharField(max_length=100,verbose_name="Nombre")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de emisión")
    payment = models.CharField(choices=CHOICES, max_length=4, verbose_name="Metodo de pago")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"

#para traducir a SQL> python manage.py makemigrations
#para mostrar el producto creado en formato sql:

#python manage.py sqlmigrate products 0001
