from django.contrib import admin
from .models import *

# Register your models here.

#TODO: EL MODELO DE DATOS PERSONALES PARA EL ADMIN HAY QUE TOQUETEARLO UN POCO
    #IDEAS: añadir dirección y usuario desde datosPersonales
class PersonalesAdmin(admin.StackedInline):
    model = DatosPersonales
    extra = 2


class TipoViaAdmin(admin.ModelAdmin):
    model = TipoVia
    list_display = ['nombre']
    search_fields = ['nombre']


class DireccionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos Base', {
            "fields": ['tipoVia', 'domicilio', 'numero']}),
        ('Datos adicionales de domicilio', {'fields': [
            'piso', 'puerta'], 'classes': ['collapse']}),
        ('Datos de ciudad', {'fields': [
            'codigoPostal', 'ciudad', 'provincia', 'pais']})
    ]

    list_display = ['tipoVia', 'domicilio', 'codigoPostal']


admin.site.register(DatosPersonales)
admin.site.register(TipoVia, TipoViaAdmin)
admin.site.register(Direccion, DireccionAdmin)
