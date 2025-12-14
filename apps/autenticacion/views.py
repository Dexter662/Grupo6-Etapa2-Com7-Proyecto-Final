from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import RegistrarUsuarioForm, IngresarUsuarioForm
# ACTUALIZADO
# Create your views here.

def registrar_usuario(request):
    if request.method == 'POST':
        #POST
        form = RegistrarUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Cuenta creada exitosamente! Ahora puedes iniciar sesión.')
            return redirect('apps.autenticacion:ingresar')
    else:
        #GET
        form = RegistrarUsuarioForm()
    
    return render(request, 'autenticacion/registrar.html', {'form': form})


def ingresar_usuario(request):
    if request.method == 'POST':
        #POST
        form = IngresarUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido, {username}!')
                return redirect('inicio')
            else:
                messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
    else:
        form = IngresarUsuarioForm()

    return render(request, 'autenticacion/ingresar.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('apps.autenticacion:ingresar')