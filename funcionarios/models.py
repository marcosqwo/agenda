from django.db import models

from clientes.models import Pessoa


class Funcionario(Pessoa):
    funcao = models.CharField('Função',max_length=35,help_text='Função na empresa')
    data_admissao = models.DateField('Admissão',help_text='Data de Admissão na empresa')



    class Meta:
        verbose_name = 'funcionário'
        verbose_name_plural = 'funcionários'


    def __str__(self):
        return super().nome