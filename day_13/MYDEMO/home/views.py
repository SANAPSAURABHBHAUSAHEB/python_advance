from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

from . import displystr

from django.template import loader

from datetime import datetime

def greet(request):
    template = loader.get_template("my.html")
    context = {
        "date": str(datetime.now()),
    }
    return HttpResponse(template.render(context, request))

def hello(request):
    return HttpResponse("Hello, world!!")

def bye(request):
    return HttpResponse("Bye Bye!!")

def name(request):
    return HttpResponse(displystr.name())