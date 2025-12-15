from django.db import models
from django.conf import settings

# Create your models here.
from django.conf import settings # Importamos settings para referenciar al User

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
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created_at'] # Ordenar por fecha de creación descendente (más reciente primero)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.author}'