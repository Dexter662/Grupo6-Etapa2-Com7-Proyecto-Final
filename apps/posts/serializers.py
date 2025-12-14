from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # Campo de lectura para mostrar el username en lugar del ID
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        # Campos que se muestran y se pueden escribir
        fields = [
            'id', 
            'author', 
            'author_username', 
            'title', 
            'content', 
            'image', 
            'created_at', 
            'updated_at'
        ]
        # Campos de solo lectura 
        read_only_fields = ['author', 'author_username', 'created_at', 'updated_at']

    # asignar automáticamente el autor al crear el post
    def create(self, validated_data):
        # El autor se toma del usuario autenticado en la solicitud (request.user)
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)