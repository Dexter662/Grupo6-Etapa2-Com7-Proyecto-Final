from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from .views import post_list, post_create, post_update, post_delete

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
    path('api/', include(router.urls)),
]