from django.contrib import admin
from Datos.models import Unidad_Medida
from Datos.models import Material
from Datos.models import Area
from Datos.models import Persona

# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
    list_display=['id','descripcion','precio']

class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display=['abreviacion','descripcion']

admin.site.register(Unidad_Medida,UnidadMedidaAdmin)
admin.site.register(Material,MaterialAdmin)
admin.site.register(Area)
admin.site.register(Persona)
