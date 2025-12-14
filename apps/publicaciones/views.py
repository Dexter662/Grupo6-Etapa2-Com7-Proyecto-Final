from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Categoria

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')  # orden por fecha descendente

    # FILTROS
    categoria = request.GET.get('categoria')
    fecha = request.GET.get('fecha')
    
    if categoria:
        posts = posts.filter(categoria_id=categoria)
    if fecha:
        posts = posts.filter(fecha_publicacion__date=fecha)

    # PAGINACION
    paginator = Paginator(posts, 5)  # 5 posts por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categorias = Categoria.objects.all()

    return render(request, 'publicaciones/lista.html', {
        'publicaciones': page_obj,
        'categorias': categorias,
        'filtro_categoria': categoria,
        'filtro_fecha': fecha,
    })


def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.all().order_by('-fecha_comentario')
    return render(request, 'publicaciones/detalle.html', {
        'post': post,
        'comentarios': comentarios
    })