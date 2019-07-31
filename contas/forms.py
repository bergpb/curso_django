from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['category'].label = "Categoria"

  class Meta:
      model = Transaction
      fields = ['date', 'description', 'value', 'notes', 'category']
      widgets = {
        'notes': forms.Textarea(attrs={'rows':4, 'cols':15}),
      }
