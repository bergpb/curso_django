from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name


class Transaction(models.Model):
    date = models.DateField('Data')
    description = models.CharField('Descrição', max_length=200)
    value = models.DecimalField('Valor', max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField('Observações', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'transação'
        verbose_name_plural = 'transações'

    def __str__(self):
        return self.description
