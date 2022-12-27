from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def task(request):
    return HttpResponse('<h1>hello boss!</h1>')

def hello(request):
    return HttpResponse('<h1><marquee>Hi!!!!!!</h1></marquee>')
