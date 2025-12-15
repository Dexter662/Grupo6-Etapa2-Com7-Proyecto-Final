from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, add_comment, delete_comment, edit_comment, post_list, post_create, post_update, post_delete, post_detail

app_name = 'posts'

# Creación del router para generar automáticamente las rutas de la API
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# Las urlpatterns del router incluyen todas las rutas CRUD para /posts/
#urlpatterns = router.urls
urlpatterns = [
    path('post/', post_list, name='lista'),
    path('crear/', post_create, name='crear'),
    path('editar/<int:pk>/', post_update, name='editar'),
    path('eliminar/<int:pk>/', post_delete, name='eliminar'),
    path('<int:pk>/', post_detail, name='detalle'),
    path('comentario/editar/<int:pk>/', edit_comment, name='editar_comentario'),
    path('comentario/eliminar/<int:pk>/', delete_comment, name='eliminar_comentario'),
    path('<int:pk>/comentar/', add_comment, name='comentar'),
    path('api/', include(router.urls)),
]