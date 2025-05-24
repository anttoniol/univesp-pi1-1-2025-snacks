from django.urls import path

from .views import (
    EstoqueListView,
    EstoqueDetailView,
    EstoqueCreateView,
    EstoqueUpdateView,
    EstoqueDeleteView,
    ProdutoListView,
    ProdutoDetailView,
    ProdutoCreateView,
    ProdutoUpdateView,
    ProdutoDeleteView,
    FornecedorListView,
    FornecedorDetailView,
    FornecedorCreateView,
    FornecedorUpdateView,
    FornecedorDeleteView,
)

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Estoque
    path("estoque/", EstoqueListView.as_view(), name="estoque-list"),
    path("estoque/<int:pk>/", EstoqueDetailView.as_view(), name="estoque-detail"),
    path("estoque/novo/", EstoqueCreateView.as_view(), name="estoque-create"),
    path("estoque/<int:pk>/editar/", EstoqueUpdateView.as_view(), name="estoque-update"),
    path("estoque/<int:pk>/excluir/", EstoqueDeleteView.as_view(), name="estoque-delete"),
    # Produto
    path("produtos/", ProdutoListView.as_view(), name="produto-list"),
    path("produtos/novo/", ProdutoCreateView.as_view(), name="produto-create"),
    path("produtos/<int:pk>/", ProdutoDetailView.as_view(), name="produto-detail"),
    path("produtos/<int:pk>/editar/", ProdutoUpdateView.as_view(), name="produto-update"),
    path("produtos/<int:pk>/excluir/", ProdutoDeleteView.as_view(), name="produto-delete"),
    # Fornecedor
    path("fornecedores/", FornecedorListView.as_view(), name="fornecedor-list"),
    path("fornecedores/novo/", FornecedorCreateView.as_view(), name="fornecedor-create"),
    path("fornecedores/<int:pk>/", FornecedorDetailView.as_view(), name="fornecedor-detail"),
    path("fornecedores/<int:pk>/editar/", FornecedorUpdateView.as_view(), name="fornecedor-update"),
    path("fornecedores/<int:pk>/excluir/", FornecedorDeleteView.as_view(), name="fornecedor-delete"),
]