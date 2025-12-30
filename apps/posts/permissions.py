from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Permite acceso de lectura (GET, HEAD, OPTIONS) a cualquiera.
    Solo permite acceso de escritura (PUT, PATCH, DELETE) al autor del objeto.
    """
    
    def has_object_permission(self, request, view, obj):
        # Permite cualquier método de lectura (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Permite métodos de escritura solo si el usuario es el autor del post
        return obj.author == request.user