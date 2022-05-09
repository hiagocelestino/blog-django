from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Comentario

def comentario(request, post_id):
    comentario = Comentario.objects.filter(post_id=post_id)
    dados = {
        'comentarios': comentario,
        'post_id': post_id
    }
    return render(request,'comentario.html', dados)

def comentar(request):
    instance = get_object_or_404(Comentario)
    form = Comentario(request.POST, instance=instance)
    if form.is_valid():
          form.save()
    
    return redirect('comentario')