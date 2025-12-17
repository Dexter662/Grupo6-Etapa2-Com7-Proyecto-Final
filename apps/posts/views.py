from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Post, Categoria, Comment
from .forms import PostForm, CommentForm, CategoriaForm
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    """
    Conjunto de vistas para CRUD de publicaciones.
    Listar, Crear, Obtener, Actualizar y Eliminar Posts.
    """
    # 1. Definir el queryset: Todos los posts, ordenados por fecha descendente
    queryset = Post.objects.all().select_related('author', 'categoria')
    # 2. Definir el serializador
    serializer_class = PostSerializer
    # 3. Definir los permisos
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


def post_list(request):
    posts = Post.objects.all().select_related('categoria', 'author')

    # 👉 Filtrado por rol
    if request.user.is_authenticated:
        if request.user.rol == 'author':
            posts = posts.filter(author=request.user)
        # admin y user ven todo

    # 👉 Filtro categoría
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        posts = posts.filter(categoria_id=categoria_id)

    # 👉 Filtro fecha
    fecha = request.GET.get('fecha')
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
    if request.user.rol not in ['admin', 'author']:
        return redirect('inicio')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
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
    post = get_object_or_404(Post, pk=pk)
    # Verificamos permisos: autor o admin
    if post.author != request.user and request.user.rol != 'admin':
        return redirect('posts:lista')

    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('posts:lista')

    return render(request, 'posts/post_form.html', {
        'form': form,
        'accion': 'Editar'
    })

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Verificamos permisos: autor o admin
    if post.author != request.user and request.user.rol != 'admin':
        return redirect('posts:lista')

    if request.method == 'POST':
        post.delete()
        return redirect('posts:lista')

    return render(request, 'posts/post_confirm_delete.html', {'post': post})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    comments_qs = post.comments.select_related('author').order_by('-created_at')
    paginator = Paginator(comments_qs, 5)
    comments = paginator.get_page(request.GET.get('page'))

    form = None
    if request.user.is_authenticated:
        form = CommentForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('posts:detalle', pk=pk)

    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()

    return redirect('posts:detalle', pk)

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    # SOLO autor del comentario o admin
    if request.user != comment.author and request.user.rol != 'admin':
        return redirect('posts:detalle', pk=comment.post.pk)

    comment.delete()
    return redirect('posts:detalle', pk=comment.post.pk)


@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    # Permisos: solo autor o admin
    if not (request.user == comment.author or request.user.rol == 'admin'):
        return redirect('posts:detalle', pk=comment.post.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('posts:detalle', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'posts/comment_edit.html', {
        'form': form,
        'comment': comment
    })

@login_required
def categoria_lista(request):
    categorias = Categoria.objects.all()
    return render(request, 'posts/categorias/categoria_list.html', {
        'categorias': categorias
    })

@login_required
def categoria_create(request):
    if request.user.rol != 'admin':
        return redirect('inicio')

    form = CategoriaForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('posts:categoria_lista')

    return render(request, 'posts/categorias/categoria_form.html', {
        'form': form,
        'accion': 'Crear'
    })


@login_required
def categoria_update(request, pk):
    if request.user.rol != 'admin':
        return redirect('inicio')

    categoria = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('posts:categoria_lista')

    return render(request, 'posts/categorias/categoria_form.html', {
        'form': form,
        'accion': 'Editar'
    })

@login_required
def categoria_delete(request, pk):
    if request.user.rol != 'admin':
        return redirect('inicio')

    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        categoria.delete()
        return redirect('posts:categoria_lista')

    return render(request, 'posts/categorias/categoria_confirm_delete.html', {
        'categoria': categoria
    })
