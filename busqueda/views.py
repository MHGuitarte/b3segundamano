from django.shortcuts import render
from productos.models import *
from productos.models import *

# Create your views here.


def index(request):
    idx = 0
    context = {'upperBanner': True, 'rightBanner': True, "products": []}
    while(idx < 4):
        art = Articulo.randomSinVender()
        img = art.imagenproducto_set.first()
        vendedor = art.vendedor.usuario.username

        titulo = art.titulo

        if len(titulo) > 16:
            titulo = titulo[:13] + "..."

        articulo = {'id': art.id, 'title': art.titulo, 'name': titulo,
                    'img': img.imagen, 'price': art.precio, 'vendor': vendedor, 'info': art.descripcion}
        if articulo not in context['products']:
            context['products'].append(articulo)
            idx += 1

    return render(request, 'inicio/inicio.html', context)


def category(request):
    context = {'upperBanner': True, 'rightBanner': True, "products": []}

    filterText = request.GET.get('id', False)

    arts = Articulo.objects.filter(categorias__nombre__contains=filterText)

    for art in arts:
        img = art.imagenproducto_set.first()
        vendedor = art.vendedor.usuario.username
        titulo = art.titulo

        if len(titulo) > 16:
            titulo = titulo[:13] + "..."

        articulo = {'id': art.id, 'title': art.titulo, 'name': titulo,
                    'img': img.imagen, 'price': art.precio, 'vendor': vendedor, 'info': art.descripcion}

        context['products'].append(articulo)

    return render(request, 'inicio/inicio.html', context)


def search(request):
    context = {'upperBanner': True, 'rightBanner': True, "products": []}

    searchText = request.GET.get('search', False)

    arts = Articulo.objects.filter(titulo__contains=searchText)

    for art in arts:
        img = art.imagenproducto_set.first()
        vendedor = art.vendedor.usuario.username
        titulo = art.titulo

        if len(titulo) > 16:
            titulo = titulo[:13] + "..."

        articulo = {'id': art.id, 'title': art.titulo, 'name': titulo,
                    'img': img.imagen, 'price': art.precio, 'vendor': vendedor, 'info': art.descripcion}

        context['products'].append(articulo)

    return render(request, 'inicio/inicio.html', context)
