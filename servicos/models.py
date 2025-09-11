from django.db import models

class Servico(models.Model):
    nome = models.CharField('Nome',max_length=100,help_text='Nome completo do serviço',unique=True)
    preco = models.DecimalField('Preço',decimal_places=2, max_digits=5,help_text='Preço do serviço')
    descricao = models.TextField('Descrição',max_length=300,help_text='Descrição e observações do serviço')


    class Meta:
        verbose_name = 'Servico'
        verbose_name_plural = 'Servicos'

    def __str__(self):
        return self.nome