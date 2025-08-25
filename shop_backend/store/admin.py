from django.contrib import admin
from .models import Product, Category, Order, OrderProduct

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(OrderProduct)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

