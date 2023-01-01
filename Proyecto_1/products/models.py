from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField()

#para traducir a SQL> python manage.py makemigrations
#para mostrar el producto creado en formato sql:

#python manage.py sqlmigrate products 0001
