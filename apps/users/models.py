from django.db import models
from django.contrib.auth.models import User

class Role(models.TextChoices):
    ADMIN = 'admin', 'Administrador'
    AUTHOR = 'author', 'Autor / Agrónomo'
    USER = 'user', 'Usuario / Agricultor'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)
    bio = models.TextField(blank=True)
    specialty = models.CharField(max_length=100, blank=True)
    # Las imágenes irán a la carpeta media/avatars
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg', blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"