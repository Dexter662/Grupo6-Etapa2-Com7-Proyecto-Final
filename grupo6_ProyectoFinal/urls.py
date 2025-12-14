"""
URL configuration for grupo6_ProyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Necesario para media
from django.conf.urls.static import static # Necesario para media

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URLS de la API V1
    path('api/v1/', include('apps.users.urls')), 
    path('api/v1/', include('apps.posts.urls')), 

    #Habilita los formularios de 'Log in' y 'Log out' de DRF
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# Servir archivos de Media (para imágenes)
# if settings.DEBUG:
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)