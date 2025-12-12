from django.urls import path
from . import views

app_name = 'apps.autenticacion'

urlpatterns = [
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('ingresar/', views.ingresar_usuario, name='ingresar'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]