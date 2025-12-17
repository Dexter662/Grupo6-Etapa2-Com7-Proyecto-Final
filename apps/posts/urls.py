from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'posts'

# Creación del router para generar automáticamente las rutas de la API
router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

# Las urlpatterns del router incluyen todas las rutas CRUD para /posts/
#urlpatterns = router.urls
urlpatterns = [
    path('', views.post_list, name='lista'),
    path('crear/', views.post_create, name='crear'),
    path('editar/<int:pk>/', views.post_update, name='editar'),
    path('eliminar/<int:pk>/', views.post_delete, name='eliminar'),
    path('<int:pk>/', views.post_detail, name='detalle'),
    path('comentario/editar/<int:pk>/', views.edit_comment, name='editar_comentario'),
    path('comentario/eliminar/<int:pk>/', views.delete_comment, name='eliminar_comentario'),
    path('<int:pk>/comentar/', views.add_comment, name='comentar'),
    path('categorias/', views.categoria_lista, name='categoria_lista'),
    path('categorias/crear/', views.categoria_create, name='categoria_crear'),
    path('categorias/<int:pk>/editar/', views.categoria_update, name='categoria_editar'),
    path('categorias/<int:pk>/eliminar/', views.categoria_delete, name='categoria_eliminar'),
    path('api/', include(router.urls)),
]