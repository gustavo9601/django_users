from django import forms
from .models import User


class UserRegiterForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
    )
    password2 = forms.CharField(
        label='Repetir Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Repetir Contraseña'})
    )

    class Meta:
        # Enlazando el modelo
        model = User
        # Especificando los campos a usar
        # fields = ('__all__')
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )
