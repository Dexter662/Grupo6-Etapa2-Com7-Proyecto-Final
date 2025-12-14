from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    """
    Conjunto de vistas para CRUD de publicaciones.
    Listar, Crear, Obtener, Actualizar y Eliminar Posts.
    """
    
    # 1. Definir el queryset: Todos los posts, ordenados por fecha descendente
    queryset = Post.objects.all().select_related('author')
    
    # 2. Definir el serializador
    serializer_class = PostSerializer
    
    # 3. Definir los permisos
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]