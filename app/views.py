from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Estoque, Produto, Fornecedor
from .forms import EstoqueForm, ProdutoForm, FornecedorForm

# Create your views here.
def index(request):
    return render(request, 'home.html')

class EstoqueListView(ListView):
    model = Estoque
    template_name = 'estoque_list.html'
    context_object_name = 'estoques'

class EstoqueDetailView(DetailView):
    model = Estoque
    template_name = 'estoque_detail.html'
    context_object_name = 'estoque'

class EstoqueCreateView(CreateView):
    model = Estoque
    form_class = EstoqueForm
    template_name = 'estoque_form.html'
    success_url = reverse_lazy('estoque-list')

class EstoqueUpdateView(UpdateView):
    model = Estoque
    form_class = EstoqueForm
    template_name = 'estoque_form.html'
    success_url = reverse_lazy('estoque-list')

class EstoqueDeleteView(DeleteView):
    model = Estoque
    template_name = 'estoque_confirm_delete.html'
    success_url = reverse_lazy('estoque-list')

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'produtos'

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'produto'

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produto-list')

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produto-list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('produto-list')

class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'fornecedor_list.html'
    context_object_name = 'fornecedores'

class FornecedorDetailView(DetailView):
    model = Fornecedor
    template_name = 'fornecedor_detail.html'
    context_object_name = 'fornecedor'

class FornecedorCreateView(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedor_form.html'
    success_url = reverse_lazy('fornecedor-list')

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedor_form.html'
    success_url = reverse_lazy('fornecedor-list')

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    template_name = 'fornecedor_confirm_delete.html'
    success_url = reverse_lazy('fornecedor-list')