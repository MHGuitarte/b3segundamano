from django.db import models
from usuarios.models import *

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=80, unique=True, blank=False)
    descripcion = models.TextField()


class ImagenProducto(models.Model):
    imagen = models.FilePathField()  # Esto hay que entenderlo bien


class Articulo(models.Model):
    titulo = models.CharField(max_length=200, blank=False)
    vendedor = models.ForeignKey(DatosPersonales, on_delete=models.PROTECT)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    # Esto habría que entenderlo mejor
    categorias = models.ManyToManyField(Categoria)
    imagenes = models.ManyToManyField(ImagenProducto)
    fechaPublicacion = models.DateTimeField()
    vendido = models.BooleanField()
