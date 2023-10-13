from django.http import HttpRequest, HttpResponse
import datetime
import datetime
from django.template import Template, Context 
from django.template import loader
from django.shortcuts import render

class Automotor:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    def getMarca(self):
        return self.marca
        

def primeraVista(request): #Fisrt View
    
    nombre = 'Ivan David Palmar Martinez'
    
    profesion = 'Aprendiz SENA'
    
    automotor1 = Automotor('Mazda',1998,15000000)
    
    automotor2 = Automotor('Ferrari',1980,1000000000)
    
    futbolistas = ['Lionel Messi','Cristiano Ronaldo','Neymar Jr']
    
    numeros = [1,2,3,4,5,6,7,8,9,10]
    
    numero2 = []
    
    listaVacia = []
    
    for i in range(0,50+1):
        numero2.append(i)
        
    fechaActual = datetime.datetime.now()
        
    templateOne = loader.get_template('primeraPlantilla.html')
    
    context = ({
        'nombreUsuario': nombre,
        'profesionUsuario': profesion,
        'fechaActual': fechaActual,
        'automotor1' : automotor1,
        'automotor2' : automotor2,
        'futbolistas': futbolistas,
        'numeros': numeros,
        'numero2' : numero2,
        'listaVacia' : listaVacia
    })
    
    document = templateOne.render(context)
    
    return HttpResponse(document) # A response

def segundaVista(request): #Second view
    return HttpResponse("Hola, soy la segunda vista") # This is the response to the request

def horaActual(request):
    
    actual = datetime.datetime.now()
    
    resultado = """<h2>
    La fecha actual es: 
    </h2> %s""" % actual

    return HttpResponse(resultado)

def edadAproximada(request, age,year):
    period = year - 2023
    futureAge = age + period
    
    response = """<html>
    <body>
    En el año: %s tendras %s años 
    </body>
    </html>
    """ %(year, futureAge)
    
    return HttpResponse(response)

#Chargers and filters
def cargadores(request):
    
    #templateTwo = open('C:/Users/FORMACION.SIBAPRSESFSD058/Documents/ivanPalmar/pythonFlashDjango/django/primerEjercicio/primerEjercicio/templates/cargadores.html')
    
    #template = Template(templateTwo.read())
    
    #templateTwo.close()
    
    nombrePersona = 'Lionel Messi'
    
    listaNombres = ['Juan','Ivan','David','Angelo','Lionel','Goku','Naruto']
    
    template = loader.get_template('cargadores.html')
        
    context = ({
        'nombrePersona' : nombrePersona,
        'listaNombres' : listaNombres
    })
    
    document = template.render(context)
    
    return HttpResponse(document)

#Metodo render y shorcuts
def plantillasIncrustadas(request):

    animales = ['Ivan','David','Goku']

    context = ({
        'animales' : animales
    })

    return render(request,'caminos.html',context)

#Herencia de plantillas
def plantillaHerencia(request):
    
    context = ({
       
    })
    
    return render(request,'herencia1.html',context)

def plantillaHerencia2(request):
    
    context = ({
        
    })
    
    return render(request, 'herencia2.html',context)