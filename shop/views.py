from django.shortcuts import render

def homepage(request):
    return render(request, 'candlehome.html')

def shop_all(request):
    return render(request, 'shopAll.html')