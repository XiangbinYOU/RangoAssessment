from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says hey there partner!")


from django.shortcuts import render

# Create your views here.
