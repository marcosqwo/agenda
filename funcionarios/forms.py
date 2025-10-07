from django import forms

from .models import Funcionario


class FuncionarioModelForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome','funcao','fone', 'email','data_admissao', 'foto']


        error_messages = {
            'nome':{'required':'O nome do funcionário(a) é um campo obrigatório'},
            'funcao':{'required':'A função do funcionário(a) é um campo obrigatório'},
            'fone':{'required':'O Telefone do funcionário(a) é um campo obrigatório'},
            'email':{'required':'Formato invalido para o E-mail. Exemplo: fulanodetal@dominio.com',
                     'unique':'E-mail já cadastrado'},
            'data_admissao':{'required':'A data de admissão é um campo obrigatório'},

        }