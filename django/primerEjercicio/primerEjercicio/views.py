from django.http import HttpRequest, HttpResponse
import datetime
import datetime
from django.template import Template, Context 

class Automotor:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        

def primeraVista(request): #Fisrt View
    
    nombre = 'Ivan David Palmar Martinez'
    
    profesion = 'Aprendiz SENA'
    
    automotor1 = Automotor('Mazda',1998,15000000)
    
    automotor2 = Automotor('Ferrari',1980,1000000000)
    
    fechaActual = datetime.datetime.now()
        
    templateOne = open('C:/Users/FORMACION.SIBAPRSESFSD058/Documents/ivanPalmar/django/primerEjercicio/primerEjercicio/templates/primeraPlantilla.html')
    
    template = Template(templateOne.read())
    
    templateOne.close()
    
    context = Context({
        'nombreUsuario': nombre,
        'profesionUsuario': profesion,
        'fechaActual': fechaActual,
        'automotor1' : automotor1,
        'automotor2' : automotor2
    })
    
    document = template.render(context)
    
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