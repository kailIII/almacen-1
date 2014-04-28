from django.db import models

# Create your models here.
class Unidad_Medida(models.Model):
    descripcion=models.CharField(max_length=100)
    abreviacion=models.CharField(max_length=20, null=True , blank=True)

    def __str__(self):
        return self.descripcion

class Material(models.Model):
    descripcion=models.CharField(max_length=100)
    precio=models.FloatField(null=True, blank=True)
    unidad=models.ForeignKey(Unidad_Medida, verbose_name='Unidad de Medida')
    def __str__(self):
        return self.descripcion

class Area(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
