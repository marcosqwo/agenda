from django import forms
from django.forms.models import inlineformset_factory

from .models import Servico, ProdutosServico


class ServicoModelForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome','descricao','preco']


        error_messages = {
            'nome':{'required': 'O nome Do serviço é um campo obrigatório',
                    'unique':'serviço ja cadastrado'},
            'descricao':{'required':'A descrição é um campo obrigatório!'},
            'preco':{'required': 'O preço Do serviço é um campo obrigatório!'}
        }


ProdutosServicoInline = inlineformset_factory(Servico,ProdutosServico,fk_name='servico',fields=('produto','quantidade'),extra=1,can_delete=True)