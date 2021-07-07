from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from busqueda.views import *


def register(request):
    return render(request, 'inicio/inicio.html', None)


def log_in(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get(
            'username', False), password=request.POST.get('pass', False))

        if user is not None:
            login(request, user)
            return redirect(index, permanent=True)
        else:
            messages.add_message(request, messages.ERROR,
                                 'TAS EQUIVOCADER DEMASIAU DIEGU')
            return redirect(index)


def log_out(request):
    logout(request)
    return redirect(index, permanent=False)
