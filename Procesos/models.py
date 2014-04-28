from django.db import models
from Datos.models import Persona
from Datos.models import Area
from Datos.models import Material
# Create your models here.

class Salida_Material(models.Model):
    fecha=models.DateField(default=date.today())
    solicitante=models.ForeingKey(Persona, verbose_name='Solicitante')
    area=models.ForeingKey(Area)
    autorizante=models.ForeingKey(Persona, verbose_name='Autorizado por')
    almacenero=models.ForeignKey(Persona,verbose_name='Encargado de almacen')
    receptor=models.ForeignKey(Persona,verbose_name='Recibido por')


    def __str__(self):
        return 'Salida de material ' + self.id

    class Meta:
        verbose_name_plural='Salidas de material'


class Item_Salida(models.Model):
    salida_material=models.ForeignKey(Salida_Material)
    material=models.ForeingKey(Material,verbose_name='Detalle')
    cantidad=models.FloatField(default=0)
    observacion=models.CharField(max_length=50)

    def __str__(self):
        return 'Detalle de salida ' + salida_material.id

    

