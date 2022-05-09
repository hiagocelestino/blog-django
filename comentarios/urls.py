from urllib.parse import urlparse
from django.urls import path, include

from . import views

urlpatterns=[
    path('comentario/<int:post_id>', views.comentario, name='comentario'),
    path('comentar', views.comentar, name='comentar'),
]