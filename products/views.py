from django.shortcuts import render


def new_product(request):
    return render(request, 'products/new-product.html')
