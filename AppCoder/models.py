from django.db import models

# Create your models here.
class Clientes(models.Model):

    nombre = models.CharField(max_length=50)
    numero_cliente = models.IntegerField()

class Repuestos(models.Model):

    nombre = models.CharField(max_length=50)
    numero_repuesto = models.IntegerField()

class Entregas(models.Model):

    cliente = models.CharField(max_length=50)
    repuesto = models.CharField(max_length=50)
    fecha_entrega = models.DateField()