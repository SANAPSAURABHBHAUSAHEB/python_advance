from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return HttpResponse("""
                        <div>
                        <h1>Hello World</h1>
                        <p>this a test server .................</p>
                        <img src="smt.jpg" alt="Italian Trulli">
                        </div>
                        """
                        )