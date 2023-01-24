from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ 
    A view to render all products in our store
    """

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, all_products.html, context)