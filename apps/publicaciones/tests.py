from django.test import TestCase
from django.utils import timezone
from .models import Post, Categoria

class PublicacionesTestCase(TestCase):
    def setUp(self):
        # Crear categoría
        self.cat1 = Categoria.objects.create(nombre='Drones')
        self.cat2 = Categoria.objects.create(nombre='Riego inteligente')

        # Crear posts
        for i in range(12):
            cat = self.cat1 if i % 2 == 0 else self.cat2
            Post.objects.create(
                titulo=f'Post {i+1}',
                contenido='Contenido de prueba',
                categoria=cat,
                fecha_publicacion=timezone.now()
            )

    def test_filtrado_categoria(self):
        """Verifica que el filtro por categoría devuelve los posts correctos"""
        posts_trigo = Post.objects.filter(categoria=self.cat1)
        self.assertEqual(posts_trigo.count(), 6)
        posts_maiz = Post.objects.filter(categoria=self.cat2)
        self.assertEqual(posts_maiz.count(), 6)

    def test_orden_fecha(self):
        """Verifica que los posts se ordenan por fecha descendente"""
        posts = Post.objects.all().order_by('-fecha_publicacion')
        self.assertTrue(posts[0].fecha_publicacion >= posts[1].fecha_publicacion)

    def test_paginacion(self):
        """Verifica que la paginación devuelve 5 posts por página"""
        from django.core.paginator import Paginator
        posts = Post.objects.all().order_by('-fecha_publicacion')
        paginator = Paginator(posts, 5)
        self.assertEqual(paginator.num_pages, 3)  # 12 posts, 5 por página = 3 páginas
        page1 = paginator.get_page(1)
        self.assertEqual(len(page1), 5)
        page3 = paginator.get_page(3)
        self.assertEqual(len(page3), 2)  # última página tiene 2 posts