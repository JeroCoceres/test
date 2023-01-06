from django.contrib import admin
from products.models import Products,Orders



@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","stock")
    list_filter = ("stock",)
    search_fields = ("name",)

@admin.register(Orders)
class Ordersadmin(admin.ModelAdmin):
    list_display = ("name","date","payment")
    search_fields = ("name",)