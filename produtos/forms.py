from django import forms

from .models import Produto


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('__all__')


        error_messages = {
            'nome':{'required': 'O nome Do produto é um campo obrigatório',
                    'unique':'produto ja cadastrado'},
            'preco':{'required': 'O preço Do produto é um campo obrigatório' },
            'quantidade' : {'required':'A quantidade em estoque do produto é um campo obrigatório'}

        }