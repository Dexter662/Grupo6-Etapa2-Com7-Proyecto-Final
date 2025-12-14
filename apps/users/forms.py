from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'specialty', 'avatar']

class UsuarioAdminEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'rol')


class ProfileAdminEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'specialty', 'avatar')