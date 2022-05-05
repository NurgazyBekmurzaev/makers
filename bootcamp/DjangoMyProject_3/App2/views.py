from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def get_main(request):
    return HttpResponse('<h1>molodec</h1>')
def get_index(requests):
    return render(requests, 'index.html', {})