from django.db import models
from usuarios.models import *

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(unique=True, blank=False)
    descripcion = models.TextField()


class Articulo(models.Model):
    titulo = models.CharField(blank=False)
    vendedor = models.ForeignKey(DatosPersonales)
    precio = models.DecimalField()
    descripcion = models.TextField()
    categorias = models.ManyToManyField(Categoria) #Esto habría que entenderlo mejor
    imagenes = models.ManyToManyField(ImagenProducto)
    fechaPublicacion = models.DateTimeField()


class ImagenProducto(models.Model):
    imagen = models.FilePathField() #Esto hay que entenderlo bien