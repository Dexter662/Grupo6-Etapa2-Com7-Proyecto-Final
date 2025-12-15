from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Comment
from .forms import CommentForm, PostForm
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from django.core.paginator import Paginator

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
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

@login_required
def post_create(request):
    if request.user.rol not in ['admin', 'author']:
        return redirect('inicio')
    
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

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 👉 TODOS los comentarios del post
    comment_list = post.comments.select_related('author').order_by('-created_at')

    # 👉 PAGINADOR (5 comentarios por página)
    paginator = Paginator(comment_list, 5)
    page_number = request.GET.get('page')
    comments = paginator.get_page(page_number)

    # 👉 Formulario
    form = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('posts:detalle', pk=post.pk)
        else:
            form = CommentForm()

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
    if not (request.user == comment.author or request.user.rol == 'admin'):
        return redirect('posts:detalle', pk=comment.post.pk)

    post_id = comment.post.id
    comment.delete()
    return redirect('posts:detalle', pk=post_id)

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