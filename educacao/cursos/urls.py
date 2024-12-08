from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.listar_cursos, name='listar_cursos'),
]
