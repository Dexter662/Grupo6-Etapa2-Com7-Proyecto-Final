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
    rol = models.CharField(
        max_length=10,
        choices=Rol.choices,
        default=Rol.USUARIO
    )

    def __str__(self):
        return f"{self.username} - {self.get_rol_display()}"
