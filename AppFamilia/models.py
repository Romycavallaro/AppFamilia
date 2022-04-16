from django.db import models

# Create your models here.
 
class Padres(models.Model):
    nombre=models.CharField(max_length=40)
    edad = models.IntegerField()

class Hermanos(models.Model):
    nombre= models.CharField(max_length=30)
    edad= models.IntegerField()

class Esposo(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeCasamiento = models.DateField()

class Hijos(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeNacimiento = models.DateField()