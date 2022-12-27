from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1>hello RAJESH...!</h1>')

def second(request):
    return HttpResponse('<h1><marquee>my second task</h1></marquee>')
