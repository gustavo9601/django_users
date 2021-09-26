from django.shortcuts import render

from django.views.generic.edit import (FormView)
from .forms import UserRegiterForm
from .models import User


# Create your views here.
class UserRegisterView(FormView):
    # Epceificando el html a rendeirzar
    template_name = 'users/register.html'
    # Especificando el formulario
    form_class = UserRegiterForm
    # Url de redireccion cuando complete
    success_url = '/'

    # Funcion que escucha el REQUEST del view
    def form_valid(self, form):
        # Creando con la funcion definida en el manager
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero'],
        )

        return super(UserRegisterView, self).form_valid(form)
