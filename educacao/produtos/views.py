from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .models import Produto

def produto_new(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('produto_sucesso')
    else:
        form = ProdutoForm()  

    return render(request, 'produtos/cadastrar_produto.html', {'form': form})

def produto_sucesso(request):
    return render(request, 'produtos/produto_sucesso.html')

