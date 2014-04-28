from django.db import models

# Create your models here.
class Material(models.Model):
    descripcion=models.CharField(max_length=100),
    precio=models.FloatField(null=True, blank=True),
    
class Unidad_Medida(models.Model):
    
