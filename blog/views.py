from django.shortcuts import render, HttpResponse

from .models import Post

# Create your views here.
def posts(request):
    primer_post = Post.objects.first()
    posts = Post.objects.all()
    return render(request, 'blogs.html', {'posts': posts, 'primer_post': primer_post}) 

def post(request, id):
    post = Post.objects.get(id=id)
   # contenido = f'{post.titulo} - {post.descripcion}'
    return render(request, 'blog.html', {'post': post}) 
