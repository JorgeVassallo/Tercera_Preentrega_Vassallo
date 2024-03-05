from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    direccion = models.CharField(max_length=35)
    telefono = models.CharField(max_length=35)
    email = models.EmailField()

    def __str__(self):

        return f"{self.nombre}, {self.apellido}"

class Sabores(models.Model):
    sabor = models.CharField(max_length=25)
    ingredientes = models.CharField(max_length=150)
    disponibilidad = models.BooleanField()

    def __str__(self):

        return f"{self.sabor}"

class Sucursales(models.Model):
    direccion = models.CharField(max_length=35)
    telefono = models.CharField(max_length=35)
    provincia = models.CharField(max_length=35)

    def __str__(self):

        return f"{self.direccion}"