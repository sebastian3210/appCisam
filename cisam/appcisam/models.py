from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length = 50)  #texto
    camada = models.IntegerField() #numero

class Pacientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()

class Profesionales(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    email = models.EmailField()


