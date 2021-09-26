from django import forms
from .models import User

from django.contrib.auth import authenticate


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

    """
    Validaciones personalizadas sobre los campos
    """

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            # añade a la cadena de errores de la vista, especificando el campo y el msm de error
            self.add_error('password2', 'No coincide la contraseñas')
        if len(self.cleaned_data['password1']) < 2:
            self.add_error('password1', 'La contraseña debe ser de mas de 2 caracteres')


# Cuando no son formularios que dependan de un modelo, se usa
# forms.Form
class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
    )

    # Validacion general para cualquier campo
    def clean(self):
        # Como no se asigna a ningun campo como tal la validacion, se debe inicial el super y retornarlo al final
        cleaned_data = super(UserLoginForm, self).clean()

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        # Verificando si se autentica correctamente
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Usuario o contraseña invalidos')

        return self.cleaned_data
