from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Clientes, Repuestos, Entregas
from datetime import date


# Create your views here.

def creo_cliente(self, nombre, numero_cliente):
    
    cliente = Clientes(nombre = nombre, numero_cliente = numero_cliente)
    
    cliente.save()

    return HttpResponse(f'Se creó correctamente el cliente {cliente.nombre} con el numero {cliente.numero_cliente}')


def creo_repuesto(self, nombre, numero_repuesto):

    repuesto = Repuestos(nombre = nombre, numero_repuesto = numero_repuesto)

    repuesto.save()

    return HttpResponse(f'Se creó correctamente el repuesto {repuesto.nombre} con el numero {repuesto.numero_repuesto}')

def creo_entrega(self, cliente, repuesto, fecha_entrega):

    entrega = Entregas(cliente = cliente, repuesto = repuesto, fecha_entrega = fecha_entrega)

    entrega.save

    return HttpResponse(f'Se creó correctamente la entrega a {entrega.cliente} del repuesto {entrega.repuesto} con fecha {entrega.fecha_entrega}')


