from rest_framework.routers import DefaultRouter
from .views import PostViewSet

# Creación del router para generar automáticamente las rutas de la API
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# Las urlpatterns del router incluyen todas las rutas CRUD para /posts/
urlpatterns = router.urls