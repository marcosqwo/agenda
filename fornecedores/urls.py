from django.urls import path

from .views import FornecedoresView, FornecedorAddView, FornecedorUpdateView, FornecedorDeleteView

urlpatterns = [
    path('fornecedores', FornecedoresView.as_view(), name='fornecedores'),
    path('fornecedores/adicionar/', FornecedorAddView.as_view(), name='fornecedor_adicionar'),
    path('<int:pk>/fornecedores/editar/', FornecedorUpdateView.as_view(), name='fornecedor_editar'),
    path('<int:pk>/fornecedores/apagar/', FornecedorDeleteView.as_view(), name='fornecedor_apagar'),

]