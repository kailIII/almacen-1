from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404
from Datos.models import Material

# Create your views here.

def index(request):
	materiales=Material.objects.all()
	return render_to_response('materiales/index.html',
		                    {'materiales': materiales})
	
def detalle(request,material_id):
	material=get_object_or_404(Material, pk=material_id)
	return render_to_response('materiales/detalle.html',
		                    {'material':material})