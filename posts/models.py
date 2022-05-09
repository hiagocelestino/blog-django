from django.db import models
from datetime import datetime
from usuario.models import Usuario
from categoria.models import Categoria

class Post(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, default=1)
    titulo = models.CharField(max_length=100)
    foto_post = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    data = models.DateField(default=datetime.now(), blank=True)
    corpo_post = models.TextField()
