from django.shortcuts import render

def index(request):
    context = {
        'title': 'Store',
        'username': 'Test Username'
    }
    return render(request, 'products/index.html', context)

def products(request):
    return render(request, 'products/products.html')