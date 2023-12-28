from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def page(request):
    return render (request, "hello/index.html")


def brian(request):
    return HttpResponse("Hello, Brian")

def greet (request, name):
    return HttpResponse(f"Hello from greet , {name.capitalize()}")


def greetWorld (request, name):
     return render (request, "hello/greet.html", {
         "name" : name.capitalize()
     })