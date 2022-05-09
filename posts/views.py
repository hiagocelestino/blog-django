from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all()

    dados = {
        'posts': posts
    }
    return render(request, 'index.html', dados)

def posts(request):
    posts= Post.objects.all()

    posts = {
        'posts' : posts
    }

    return render(request,'post.html', posts)

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    post_a_exibir = {
        'post' : post
    }

    return render(request,'post.html', post_a_exibir)