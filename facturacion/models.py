from django.db import models

# Create your models here.

class TipoIVA( models.Model ):
    descripcion = models.CharField( max_length = 100 )
    tipoImpositivo = models.DecimalField( max_length = 5, decimal_places = 2 )
    desde = models.DateTimeField( auto_now = True )
    hasta = models.DateTimeField( null = True )

class LineaFactura( models.Model ):
    pass

class Factura( models.Model ):
    fechaEmision = models.DateField( auto_now = True )
    fechaPago = models.DateField( null = True )
    cliente = models.ForeignKey( "usuarios_usuario" )
    numero = models.IntegerField( unique_for_year = True, editable = False, )
    """
    TODO:
        ¿Campos calculados?
    """