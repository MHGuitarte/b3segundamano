from django.db import models
from django.contrib.auth.models import User

# Modelos que no vamos a usar

"""
class TiposPremium( models.Model ):
    descripcion = models.CharField( max_length = 200 )
    precio = models.DecimalField( max_digits = 5, decimal_places = 2 )
    desde = models.DateTimeField( auto_now = True )
    hasta = models.DateTimeField( null = True )

class Premium( models.Model ):
    tipo = models.ForeignKey( TiposPremium )
    vencimiento = models.DateTimeField( auto_now = True )
    pagado = models.DecimalField()

class Comentario( models.Model ):
    STAR_NUMBER = [
        ( 1, 'Ni para comprá pan' ),
        ( 2, 'Ni pa ti ni pa mi' ),
        ( 3, 'Tú sabe' ),
        ( 4, '¡Que güeno pisha!' ),
        ( 5, '¡Canelita en rama!' )
    ]
    comentario = models.TextField( blank = True )
    estrellas = models.PositiveSmallIntegerField( default = 5, 
                choices = STAR_NUMBER )
    fecha = models.DateTimeField( auto_now = True )
    quien = models.ForeignKey( Usuario )

class Domicilio( models.Model ):
    pass

class Usuario( models.Model ):
    auth = models.ForeignKey( "auth_user" )
    nif = models.CharField( max_length = 9, unique = True, blank = False, 
                    help_text = "sólo letras y número, es decir, sin espacios ni signos de puntuación alguno" )
    premium = models.ForeignKey( Premium )
    valoraciones = models.ForeignKey( Comentario )
    correos = models.ForeignKey( Correo )
    domicilios = models.ForeignKey( Domicilio )

"""

# REVISIÓN 0.1


class TipoVia(models.Model):
    nombre = models.CharField(
        max_length=20, unique=True, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)


class Direccion(models.Model):
    tipoVia = models.ForeignKey(
        TipoVia, on_delete=models.PROTECT)
    domicilio = models.CharField(max_length=200, blank=False)
    numero = models.CharField(max_length=2)
    piso = models.CharField(max_length=2)
    puerta = models.CharField(max_length=2)
    codigoPostal = models.CharField(max_length=5)
    ciudad = models.CharField(max_length=80)
    provincia = models.CharField(max_length=30)
    pais = models.CharField(max_length=20)


class DatosPersonales(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40, blank=False)
    apellidos = models.CharField(max_length=160, blank=False)
    documento = models.CharField(max_length=9, unique=True, blank=False)
    telefono = models.CharField(max_length=13, unique=True, blank=True)
    correo = models.EmailField(unique=True, blank=False)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    baja = models.BooleanField()
