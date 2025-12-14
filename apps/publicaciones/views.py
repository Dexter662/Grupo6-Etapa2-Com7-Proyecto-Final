from django.shortcuts import render
from .models import Post

def lista_posts(request):
    categoria = request.GET.get('categoria')
    fecha = request.GET.get('fecha')

    posts = Post.objects.all()

    if categoria:
        posts = posts.filter(categoria__nombre__icontains=categoria)

    if fecha:
        posts = posts.filter(fecha_publicacion=fecha)

    return render(request, 'publicaciones/lista.html', {'posts': posts})