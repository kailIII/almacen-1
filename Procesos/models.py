from django.db import models
from Datos.models import Persona
from Datos.models import Area
from Datos.models import Material
from datetime import date
from django.db import models
from django.contrib import admin
# Create your models here.

class Salida_Material(models.Model):
    fecha=models.DateField(default=date.today())
    solicitante=models.ForeignKey(Persona,related_name='solicitante', verbose_name='Solicitante')
    autorizante=models.ForeignKey(Persona,related_name='autorizante', verbose_name='Autorizado por')
    almacenero=models.ForeignKey(Persona,related_name='almacenero',verbose_name='Encargado de almacen')
    receptor=models.ForeignKey(Persona,related_name='receptor',verbose_name='Recibido por')
    
    
    def __str__(self):
        return 'Salida de material ' + str(self.id)

    

    class Meta:
        verbose_name_plural='Salidas de material'
        verbose_name='Salida de material'


class Item_Salida(models.Model):
    salida_material=models.ForeignKey(Salida_Material)
    material=models.ForeignKey(Material,verbose_name='Material')
    def _getPrecio(self):
        return self.material.precio

    def undMed(self):
        return self.material.unidad.descripcion
    
    
    precio=property(_getPrecio)
    unidad=property(undMed)
    cantidad=models.FloatField(default=0)

    def total(self):
        return self.material.precio*self.cantidad
    observacion=models.CharField(max_length=200,default='NINGUNA')

    def __str__(self):
        return 'Detalle de salida ' + str(self.salida_material.id)

    class Meta:
        verbose_name='Detalle de Salida'
        verbose_name_plural='Detalle de Salida'

    


class Registro(models.Model):
    fecha=models.DateField('Fecha de ingreso',default=date.today())
    material=models.ForeignKey(Material)
    ingreso=models.IntegerField('Ingreso',default=0)
    stock=models.IntegerField(default=0)
    observacion=models.TextField(max_length=200,default='NINGUNA')
    autorizante=models.ForeignKey(Persona,verbose_name='Autorizado Por')
    
    def __str__(self):
        return 'Registro ' + str(self.id)






    



