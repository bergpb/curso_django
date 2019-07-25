from django.forms import ModelForm, Textarea
from .models import Transaction

class TransactionForm(ModelForm):
  class Meta:
      model = Transaction
      fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']
      widgets = {
        'observacoes': Textarea(attrs={'rows':4, 'cols':15}),
      }
