from django import forms

from .models import Servico


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