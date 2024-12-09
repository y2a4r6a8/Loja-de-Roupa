from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.lista_categorias, name="lista_categorias"),
    path('categorias/novo/', views.nova_categoria, name="nova_categoria"),
    path('categorias/editar/<int:id>/', views.edita_categoria, name="edita_categoria"),
    path('categorias/remover/<int:id>/', views.remove_categoria, name="remove_categoria"),
    path('produtos/', views.lista_produtos, name="lista_produtos"),
    path('produtos/novo/', views.novo_produto, name="novo_produto"),
    path('produtos/editar/<int:id>/', views.edita_produto, name="edita_produto"),
    path('produtos/remover/<int:id>/', views.remove_produto, name="remove_produto"),
]
