from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicar clase Bootstrap a todos los campos
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class IngresarUsuarioForm(forms.Form):
    username = forms.CharField(
        label="Nombre de Usuario",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )
