from django.contrib import admin
from django.urls import path, include
from .views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('publicaciones/', include('apps.publicaciones.urls')),
    path('autenticacion/', include('apps.autenticacion.urls'))
]