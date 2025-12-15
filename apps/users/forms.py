from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'specialty', 'avatar']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'specialty': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

class UsuarioAdminEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'rol')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'rol': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
