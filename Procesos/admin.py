from django.contrib import admin
from Procesos.models import Salida_Material
from Procesos.models import Item_Salida
from Procesos.models import Registro


# Register your models here.

class Item_SalidaInline(admin.TabularInline):
    model=Item_Salida
    readonly_fields = ('precio','unidad','total',)
        
    
class Salida_MaterialAdmin(admin.ModelAdmin):
    
    list_display=['id','fecha','solicitante','autorizante','receptor']    
    inlines = [
        Item_SalidaInline,
    ]


class RegistroAdmin(admin.ModelAdmin):
    
    list_display=['id','fecha','material','stock','observacion']    
    
admin.site.register(Salida_Material,Salida_MaterialAdmin)
admin.site.register(Registro,RegistroAdmin)




