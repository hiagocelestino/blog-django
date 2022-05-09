from time import timezone
from django.db import models
from datetime import datetime
from posts.models import Post

class Comentario(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, default=1)
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    corpo_comentario = models.TextField()
    data = models.DateField(default=datetime.now(), blank=True)
