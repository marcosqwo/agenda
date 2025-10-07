from django import forms

from .models import Cliente


class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco','fone', 'email', 'foto']


        error_messages = {
            'nome':{'required':'O nome do cliente é um campo obrigatório'},
            'endereco':{'required':'O endereço do cliente é um campo obrigatório'},
            'fone':{'required':'O Telefone do cliente é um campo obrigatório'},
            'email':{'required':'Formato invalido para o E-mail. Exemplo: fulanodetal@dominio.com',
                     'unique':'E-mail já cadastrado'},

        }