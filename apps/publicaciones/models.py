from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def _str_(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def _str_(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def _str_(self):
        return f"Comentario de {self.autor}"