from django.shortcuts import render
from django.http import HttpResponse

def get_main(request):
    return HttpResponse('<h1>hello</h1>')
