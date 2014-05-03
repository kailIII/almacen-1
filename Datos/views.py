from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404,redirect
from Datos.models import Material,Area
from django.template import RequestContext
from Datos.form import AreaForm


# Create your views here.

def index(request):
	materiales=Material.objects.all()
	return render_to_response('materiales/index.html',
		                    {'materiales': materiales})
	
def detalle(request,material_id):
	material=get_object_or_404(Material, pk=material_id)
	return render_to_response('materiales/detalle.html',
		                    {'material':material})


def area_crear(request):
	if request.method=="POST":
	   form=AreaForm(request.POST)
	   #name=form.cleaned_data['nombre']
	   name=""
	   if name=="SISTEMAS":
		     Area.objects.filter(name="RRHH").update(nombre="name")
	   else:
			 area=Area(nombre=form.cleaned_data['nombre'])
			 area.save()
	   return redirect ('materiales')
	else:
	    form=AreaForm()	
	return render_to_response('materiales/area_crear.html',
		{'form':form},
	context_instance=RequestContext(request))


	