from django.shortcuts import render, HttpResponse

#Modelos
from .models import Project

# Create your views here.
def perfil(request):
    #p1 = Project(titulo="Curso de HTML",  descripcion = "Descripcion del Curso HTML" )
    #p1.save()

    #p2 = Project(titulo="Curso de CSS",  descripcion = "Descripcion del Curso CSS" )
    #p2.save()

    #p3 = Project(titulo="Curso de Python",  descripcion = "Descripcion del Curso Python" )
    #p3.save()
    
    projects = Project.objects.all()

    
    return render(request, 'perfil.html', {'projects': projects}) 

