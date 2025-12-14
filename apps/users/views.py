from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .models import Role

def es_autor(user):
    return user.is_authenticated and user.profile.role == Role.AUTHOR

@user_passes_test(es_autor)
def vista_solo_autores(request):
    return HttpResponse("Acceso permitido: sos AUTOR")
