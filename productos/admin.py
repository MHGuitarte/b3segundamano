from django.contrib import admin
from productos.models import *
# Register your models here.


class ImagenInline(admin.StackedInline):
    model = ImagenProducto
    extra = 3

    list_display = ['articulo', 'fechaSubida']


class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria
    list_display = ['nombre']
    search_field = ['nombre']


class ArticuloAdmin(admin.ModelAdmin):
    model = Articulo

    fieldsets = [
        (None, {
            "fields": ['titulo', 'vendedor', 'precio']}),
        ('Datos Adicionales', {"fields": ['categorias', 'descripcion'],
                'classes': ['extrapretty', 'collapse']}),
        (None, {"fields": ['vendido']})
    ]

    inlines = [ImagenInline]
    list_display = ['titulo', 'vendedor', 'fechaPublicacion']


admin.site.register(ImagenProducto)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Articulo, ArticuloAdmin)
