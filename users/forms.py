from django.forms import ModelForm, EmailField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# reescrevendo a classe de registro de usuário
class UserResgiterForm(UserCreationForm):
  email = EmailField()

  # remove helper_text na tela de registro
  def __init__(self, *args, **kwargs):
        super(UserResgiterForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
