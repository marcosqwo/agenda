from django.contrib import admin
from django.utils.html import format_html

from clientes.models import Cliente


@admin.register(Cliente)
class FornecedorAdmin(admin.ModelAdmin):
    fields = ('nome', 'endereco','fone','email','foto','fotografia')
    list_display = ('nome','endereco','email')
    search_fields = ('nome','fone')
    readonly_fields = ['fotografia',]

    def fotografia(self,obj):
        if obj.foto:
            return format_html('<img width="75px" src="{}" />',obj.foto)
        pass