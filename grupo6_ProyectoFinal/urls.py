from django.contrib import admin
from django.urls import path, include
from .views import inicio
from django.conf import settings # Necesario para media
from django.conf.urls.static import static # Necesario para media

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', inicio, name="inicio"),
    #path('publicaciones/', include('apps.publicaciones.urls')),
    path('autenticacion/', include('apps.autenticacion.urls')),
    
    path('', include('apps.posts.urls')),
    path('api/',  include('apps.posts.urls')),

    # URLS de la API V1
    path('api/v1/', include('apps.users.urls')), 
    path('api/v1/', include('apps.posts.urls')), 

    #Habilita los formularios de 'Log in' y 'Log out' de DRF
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# Servir archivos de Media (para imágenes)
# if settings.DEBUG:
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

