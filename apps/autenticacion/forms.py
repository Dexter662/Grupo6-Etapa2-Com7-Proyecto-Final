from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2', 'avatar', 'biografia', 'especialidad')

class IngresarUsuarioForm(forms.Form):
    username = forms.CharField(label="Nombre de Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)