from django import forms

from .models import Fornecedor


class FornecedorModelForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'


        error_messages = {
            'nome': {'required':'O nome é um campo obrigatório'},
            'cnpj': {'required':'O Cnpj é um campo obrigatório','unique':'Cnpj ja cadastrado'},
            'fone': {'required':'O numero do telefone é um campo obrigatório'},

        }