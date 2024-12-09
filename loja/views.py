from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Produto

def tela_inicial(request):
    return render(request, 'loja/tela_inicial.html')
    
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'loja/lista_categorias.html', {'categorias': categorias})

def nova_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        Categoria.objects.create(nome=nome)
        return redirect('lista_categorias')
    return render(request, 'loja/nova_categoria.html')

def edita_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.nome = request.POST.get('nome')
        categoria.save()
        return redirect('lista_categorias')
    return render(request, 'loja/edita_categoria.html', {'categoria': categoria})

def remove_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('lista_categorias')

# Produto CRUD
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/lista_produtos.html', {'produtos': produtos})

def novo_produto(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        categoria_id = request.POST.get('categoria')
        categoria = get_object_or_404(Categoria, id=categoria_id)
        Produto.objects.create(nome=nome, descricao=descricao, preco=preco, quantidade=quantidade, categoria=categoria)
        return redirect('lista_produtos')
    return render(request, 'loja/novo_produto.html', {'categorias': categorias})

def edita_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        produto.quantidade = request.POST.get('quantidade')
        categoria_id = request.POST.get('categoria')
        produto.categoria = get_object_or_404(Categoria, id=categoria_id)
        produto.save()
        return redirect('lista_produtos')
    return render(request, 'loja/edita_produto.html', {'produto': produto, 'categorias': categorias})

def remove_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('lista_produtos')
