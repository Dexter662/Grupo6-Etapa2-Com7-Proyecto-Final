from django.urls import path
from .views import registrar_usuario, ingresar_usuario, confirmar_logout, cerrar_sesion

app_name = 'apps.autenticacion'

urlpatterns = [
    path('registrar/', registrar_usuario, name='registrar'),
    path('ingresar/', ingresar_usuario, name='ingresar'),
    path('cerrar-sesion/', confirmar_logout, name='confirmar_logout'),
    path('cerrar-sesion/confirmar/', cerrar_sesion, name='cerrar_sesion'),
]