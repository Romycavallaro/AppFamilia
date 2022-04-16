from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from AppFamilia.models import Padres, Hermanos, Esposo, Hijos
# Create your views here.



def titulo(request):
    return HttpResponse("Mi Familia")

def probandoTemplate(self):

    nombre = "Romina"
    apellido = "Cavallaro"

    diccionario = {"nombre": nombre, "apellido": apellido}
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)


def padre(self):
    padre = Padres(nombre = "Liliana", edad = "67")
    padre.save()
    documentoDeTexto = f"--->Madre:{padre.nombre}, Edad:{padre.edad}"
    return HttpResponse(documentoDeTexto)

def hermano(self):
    hermano1 = Hermanos(nombre = "Emiliano", edad = "40")
    hermano1.save()

    hermano2 = Hermanos(nombre = "Agustin", edad = "35")
    hermano2.save()

    hermano3 = Hermanos(nombre = "Nadia", edad = "32")
    hermano3.save()

    documentoDeTexto = f"--->Hermano:{hermano1.nombre}, Edad:{hermano1.edad}" + f"--->Hermano:{hermano2.nombre}, Edad:{hermano2.edad}" + f"--->Hermano:{hermano3.nombre}, Edad:{hermano3.edad}"
    return HttpResponse(documentoDeTexto)

def esposo(self):
    esposo = Esposo(nombre = "Diego", fechaDeCasamiento= "2016-4-9")
    esposo.save()
    documentoDeTexto = f"--->Esposo:{esposo.nombre}, Fecha de Casamiento:{esposo.fechaDeCasamiento}"
    return HttpResponse(documentoDeTexto)

def hijo(self):
    hijo1 = Hijos (nombre = "Dante", fechaDeNacimiento= "2019-1-31")
    hijo1.save()

    hijo2 = Hijos (nombre = "Antonio", fechaDeNacimiento= "2019-8-8")
    hijo2.save()
    documentoDeTexto = f"--->Hijo:{hijo1.nombre}, Fecha de Nacimiento:{hijo1.fechaDeNacimiento}" + f"--->Hijo:{hijo2.nombre}, Fecha de Nacimiento:{hijo2.fechaDeNacimiento}"
    return HttpResponse(documentoDeTexto)