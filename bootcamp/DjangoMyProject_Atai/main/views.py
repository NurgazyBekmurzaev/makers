from django.shortcuts import render
from django.http import HttpResponse
from main.models import  Category, Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'product.html', locals())
def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})




