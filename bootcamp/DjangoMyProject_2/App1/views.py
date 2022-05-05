from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def get_main(request):
    return HttpResponse('<h1>Success</h1>')
def get_elements(requests):
    return render(requests, 'elements.html', {})
def get_generic(requests):
    return render(requests, 'generic.html', {})
def get_index(requests):
    return render(requests, 'index.html', {})