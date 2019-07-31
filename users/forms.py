from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


# rewriting register class from user
class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()

  # remove helper_text on register
  def __init__(self, *args, **kwargs):
    super(UserRegisterForm, self).__init__(*args, **kwargs)
    for fieldname in ['username', 'email', 'password1', 'password2']:
      self.fields[fieldname].help_text = None

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # remove helper_text on screen to update a profile
    def __init__(self, *args, **kwargs):
      super(UserUpdateForm, self).__init__(*args, **kwargs)
      self.fields['username'].help_text = None
          

    class Meta:
      model = User
      fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(ProfileUpdateForm, self).__init__(*args, **kwargs)
    self.fields['image'].label = "Imagem"

  class Meta:
    model = Profile
    fields = ['image']
