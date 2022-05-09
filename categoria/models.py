from django.db import models

class Categoria(models.Model):
    dsc_categoria = models.CharField(max_length=50)