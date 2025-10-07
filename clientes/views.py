from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from clientes.forms import ClienteModelForm

from clientes.models import Cliente


class ClienteView(PermissionRequiredMixin,ListView):
    permission_required = 'clientes.view_cliente'
    permission_denied_message = 'visualizar cliente'

    model = Cliente
    template_name = 'clientes.html'


    def get_queryset(self):
        buscar=self.request.GET.get('buscar')
        qs = super(ClienteView,self).get_queryset()
        if buscar:
           qs=qs.filter(nome__icontains=buscar)
        if qs.count()>0:
            paginator = Paginator(qs,1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem Clientes cadastrados!')


class ClienteAddView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'clientes.add_cliente'
    permission_denied_message = 'Adicionar cliente'
    model = Cliente
    form_class = ClienteModelForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')
    success_message = 'Cliente criado com sucesso!'


class ClienteUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'clientes.update_cliente'
    permission_denied_message = 'Editar cliente'
    model = Cliente
    form_class = ClienteModelForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')
    success_message = 'Cliente atualizado com sucesso!'

class ClienteDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'clientes.delete_cliente'
    permission_denied_message = 'excluir cliente'
    model = Cliente
    template_name = 'cliente_apagar.html'
    success_url = reverse_lazy('clientes')
    success_message = 'Cliente deletado com sucesso!'

    def post(self , request , *args , **kwargs ):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            return super().post(request , *args , **kwargs )
        except ProtectedError:
            messages.error(request , f'O cliente {self.object} não pode ser excluido.'
                           f'Esse cliente está registrado em agendamentos')

        finally:
            return redirect(success_url)