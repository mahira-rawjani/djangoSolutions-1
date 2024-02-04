from django.shortcuts import render
from .models import Product

def homepage(request):
    return render(request, 'candlehome.html')

def shop_all(request):
    products = Product.objects.all()
    return render(request, 'shopAll.html', {'products': products})