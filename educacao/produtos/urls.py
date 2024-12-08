from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.produto_new, name='produto_new'),
    path('sucesso/', views.produto_sucesso, name='produto_sucesso'),
]
