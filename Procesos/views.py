from django.shortcuts import render
from Datos import Salida_Material

# Create your views here.

def obtenerMaterial(request):
    materiales=Material.objects.all()

    return render_to_response('inicio.html',{'materiales':materiales})

  
    
