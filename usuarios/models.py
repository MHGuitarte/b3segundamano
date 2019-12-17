from django.db import models

# Create your models here.

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
