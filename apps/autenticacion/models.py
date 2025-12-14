# models.py en el app "autenticacion"
#ACTUALIZADO
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

#ACTUALIZADO
class Rol(models.TextChoices):
    ADMIN = 'admin', 'Administrador'
    AUTOR = 'author', 'Autor / Agrónomo'
    USUARIO = 'user', 'Usuario / Agricultor'


class Usuario(AbstractUser):
    rol = models.CharField(max_length=10, choices=Rol.choices, default=Rol.USUARIO)
    biografia = models.TextField(blank=True)
    especialidad = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='usuarios/', default='usuarios/default.png')

    def obtener_url(self):
        return reverse('inicio')

    def __str__(self):
        return f"{self.username} - {self.get_rol_display()}"
