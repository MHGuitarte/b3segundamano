from django.db import models

# Create your models here.

class Premium( models.Model ):
    pass

class Comentario( models.Model ):
    comentario = models.TextField( blank = True )
    estrellas = models.SmallIntegerField()

class Usuario( models.Mode ):
    auth = models.ForeignKey( "auth_user" )
    nif = models.CharField( max_length = 9, unique = True, blank = False, 
                    help_text = "sólo letras y número, es decir, sin espacios ni signos de puntuación alguno" )
    premium = models.ForeignKey( Premium )
    valoraciones = models.ForeignKey( Comentario )
    correos = models.ForeignKey( Correo )
