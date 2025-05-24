from django import forms
from .models import Estoque, Produto, Fornecedor

class EstoqueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_produto'].empty_label = 'Selecione um produto'
        self.fields['id_fornecedor'].empty_label = 'Selecione um fornecedor'
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = (existing_classes + ' form-campo').strip()
    class Meta:
        model = Estoque
        fields = '__all__'
        widgets = {
            'data_validade': forms.DateInput(attrs={'type': 'date'})
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'
