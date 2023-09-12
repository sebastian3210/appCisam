from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader


def saludo(request):
    return HttpResponse('hola cisam')

def dia_hoy(request):
    hoy = datetime.now()

    respuesta = f"<h1>hoy es {hoy} <h1/>"
    return HttpResponse(respuesta)

def anio_nacimiento(request, edad):

    edad = int(edad)

    anio_nac = datetime.now().year - edad
    return HttpResponse(f"Naciste en el  {anio_nac}")

def vista_plantilla(request):
    #abrimos el archivo
    archivo = open("/Users/Sebastian/Desktop/appCisam/cisam/cisam/templates/plantilla.html")  
    # creamos le objeto "plantilla"
    plantilla = Template(archivo.read())
    #cerramos le archivo para liberar recursos
    archivo.close()

    #diccionario con datos
    datos = {"nombre":"Sebastian", "fecha": datetime.now(), "apellido": "Pastor", "edad": "24"}

    #creamos el contexto
    contexto = Context(datos)

    #renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)

    #retornamos la respuesta
    return HttpResponse(documento)

def vista_listado_alumnos(request):
    archivo = open("/Users/Sebastian/Desktop/appCisam/cisam/cisam/templates/listado_alumnos.html")

    plantilla = Template(archivo.read())

    archivo.close()

    listado_alumnos = ["Sebastian Pastor", "Guillermo Musante", "Viviana Jin", "Maria Jose Gasparini", "cindy fong", "Claudio Ortiz", "diego Paretti", "Francisco Valusek", "Marcos Bermudez", 'Martin bermudez']

    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)
    
def vista_listado_alumnos2(request):
    listado_alumnos = ["Sebastian Pastor", "Guillermo Musante", "Viviana Jin", "Maria Jose Gasparini", "cindy fong", "Claudio Ortiz", "diego Paretti", "Francisco Valusek", "Marcos Bermudez", 'Martin bermudez']

    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}

    plantilla = loader.get_template("listado_alumnos.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)
        
