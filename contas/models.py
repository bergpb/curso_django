from django.db import models


class Category(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_atualizacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome


class Transaction(models.Model):
    data = models.DateField()
    descricao = models.CharField('Descrição', max_length=200)
    valor = models.DecimalField('Valor', max_digits=7, decimal_places=3)
    categoria = models.ForeignKey('Category', on_delete=models.CASCADE)
    observacoes = models.TextField('Observações', null=True, blank=True)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_atualizacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'transação'
        verbose_name_plural = 'transações'

    def __str__(self):
        return self.descricao
