from django.urls import path
from . import views

app_name = 'publicaciones'

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('post/<int:pk>/', views.detalle_post, name='detalle_post'),
]