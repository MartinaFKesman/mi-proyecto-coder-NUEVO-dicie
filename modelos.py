from urls import urlpatterns
from django.apps import modelos 

from unittest.util import _MAX_LENGTH
from django.db import models

class Venta(modelos.Model):
    remeras = modelos.CharField(_MAX_LENGTH= 40 )
    pantalones = modelos.CharField(_MAX_LENGTH= 40)
    camisas = modelos.CharField(_MAX_LENGTH= 40)


class Compra(modelos.Model):
    remeras = modelos.CharField(max_length= 40)
    pantalones = modelos.CharField(max_lenght= 40)
    camisas = modelos.CharField(max_lenght= 40 )
    accesorios = modelos.CharField(max_lenght = 30)
    

class Donaciones(modelos.Model):
    ropa = ("remeras,pantalones, camisas, accesorios") 
def Donaciones (requiered: ) 
    
    
    
    