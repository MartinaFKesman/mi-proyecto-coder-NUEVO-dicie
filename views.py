from django.shortcuts import render 
from modelos import Compra
from django.http import HttpResponse
from modelos import Inicio 
from django.template import Context, Template 

def loginView(request):
    print("method: ", request.method)
    print("post: ", request.post)


    if request.method == "POST"
    
    