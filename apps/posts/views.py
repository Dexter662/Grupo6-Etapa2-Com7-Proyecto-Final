from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Categoria
from .forms import PostForm
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    """
    Conjunto de vistas para CRUD de publicaciones.
    Listar, Crear, Obtener, Actualizar y Eliminar Posts.
    """
    # 1. Definir el queryset: Todos los posts, ordenados por fecha descendente
    queryset = Post.objects.all().select_related('author')
    # 2. Definir el serializador
    serializer_class = PostSerializer
    # 3. Definir los permisos
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


def post_list(request):
    posts = Post.objects.all().select_related('categoria')

    categoria_id = request.GET.get('categoria')
    fecha = request.GET.get('fecha')

    if categoria_id:
        posts = posts.filter(categoria_id=categoria_id)

    if fecha:
        posts = posts.filter(created_at__date=fecha)

    categorias = Categoria.objects.all()

    return render(request, 'posts/post_list.html', {
        'posts': posts,
        'categorias': categorias,
        'categoria_seleccionada': categoria_id,
        'fecha_seleccionada': fecha,
    })

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user   # 👈 CLAVE
            post.save()
            return redirect('posts:lista')
    else:
        form = PostForm()

    return render(request, 'posts/post_form.html', {
        'form': form,
        'accion': 'Crear'
    })

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:lista')
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/post_form.html', {
        'form': form,
        'accion': 'Editar'
    })

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == 'POST':
        post.delete()
        return redirect('posts:lista')

    return render(request, 'posts/post_confirm_delete.html', {
        'post': post
    })
