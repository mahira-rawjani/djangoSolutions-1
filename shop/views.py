from django.shortcuts import render
from .models import Product

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def homepage(request):
    return render(request, 'candlehome.html')

def shop_all(request):
    products = Product.objects.all()
    return render(request, 'shopAll.html', {'products': products})