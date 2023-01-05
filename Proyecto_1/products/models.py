from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField()


class Orders(models.Model):
    CHOICES = (
        ("Card","Card"),
        ("Cash","Cash"),
    )
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    payment = models.CharField(choices=CHOICES, max_length=4)


#para traducir a SQL> python manage.py makemigrations
#para mostrar el producto creado en formato sql:

#python manage.py sqlmigrate products 0001
