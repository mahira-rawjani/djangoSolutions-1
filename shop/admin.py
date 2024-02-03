from django.contrib import admin
from shop.models import Category, Product, Customer, OrderDetails

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(OrderDetails)