from django.contrib import admin
from Datos.models import Unidad_Medida
from Datos.models import Material
from Datos.models import Area
from Datos.models import Persona

# Register your models here.



admin.site.register(Unidad_Medida)
admin.site.register(Material)
admin.site.register(Area)
admin.site(Persona)
