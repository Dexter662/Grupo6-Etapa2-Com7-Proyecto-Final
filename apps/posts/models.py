from django.db import models
from django.conf import settings # Importamos settings para referenciar al User

# Agrego modelo de categoria

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    creada = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def _str_(self):
        return self.nombre

class Post(models.Model):
    """
    Modelo para representar una publicación.
    """
    
    # El User que creó la publicación. Usamos settings.AUTH_USER_MODEL 
    # para referenciar al modelo User personalizado (apps.users.User).
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    
    title = models.CharField(max_length=255, verbose_name='Título')
    
    content = models.TextField(verbose_name='Contenido')
    
    image = models.ImageField(
        upload_to='posts_images/',
        blank=True,
        null=True,
        verbose_name='Imagen de la Publicación'
    )

    categoria = models.ForeignKey(  #nuevo agregado
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='Categoría'
    )
       
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created_at'] # Ordenar por fecha de creación descendente (más reciente primero)

    def __str__(self):
        return self.title