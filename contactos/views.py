from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contacto
# Create your views here.

def index(request):
    contactos = Contacto.objects.all()[:10]
    context = {'contactos':contactos}
    return render(request,'index.html',context)

def detalles(request, telefono):
    contacto = Contacto.objects.get(telefono=telefono)
    context = {'contacto':contacto}
    return render(request,'detalle.html',context)
    
def agregar(request):
    if(request.method == 'POST'):
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        
        contacto = Contacto(nombre=nombre, apellido=apellido, telefono=telefono)
        contacto.save()
        
        return redirect('/contactos')
        
    else:
        return render(request, 'agregar.html')
    
