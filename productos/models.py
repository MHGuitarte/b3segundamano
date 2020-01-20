from django.db import models
from django.db.models import Max
from random import randint
from usuarios.models import *

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=80, unique=True, blank=False)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    titulo = models.CharField(max_length=200, blank=False)
    vendedor = models.ForeignKey(DatosPersonales, on_delete=models.PROTECT)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    categorias = models.ManyToManyField(Categoria)
    fechaPublicacion = models.DateTimeField(auto_now=True)
    vendido = models.BooleanField()

    def __str__(self):
        return self.titulo

    def randomSinVender():
        max_id = Articulo.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = randint(1, max_id)
            articulo = Articulo.objects.filter(pk=pk).first()
            if articulo and articulo.vendido != True:
                return articulo


class ImagenProducto(models.Model):
    imagen = models.ImageField()
    fechaSubida = models.DateTimeField(auto_now_add=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)

    def __str__(self):
        return str('{art} - {fecha}'.format(art=self.articulo.titulo, fecha=self.fechaSubida))
