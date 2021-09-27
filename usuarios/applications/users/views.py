from django.shortcuts import render

from django.views.generic.edit import (FormView, View)
from .forms import UserRegiterForm, UserLoginForm
from .models import User
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout


# Create your views here.
class UserRegisterView(FormView):
    # Epceificando el html a rendeirzar
    template_name = 'users/register.html'
    # Especificando el formulario
    form_class = UserRegiterForm
    # Url de redireccion cuando complete
    success_url = reverse_lazy('home:inicio')

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


class LoginUserView(FormView):
    # Epceificando el html a rendeirzar
    template_name = 'users/login.html'
    # Especificando el formulario
    form_class = UserLoginForm
    # Url de redireccion cuando complete
    success_url = reverse_lazy('home:inicio')

    # Funcion que escucha el REQUEST del view
    def form_valid(self, form):
        # Usando la autenticacion propia de django
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        # autentica al usuario y deja la sesion global de ese usuario
        login(self.request, user)

        return super(LoginUserView, self).form_valid(form)


# View => es el padre de todas las vistas
class LogoutUserView(View):
    # metodo GET por la url
    def get(self, request, *args, **kwargs):
        # Cierra la sesion
        logout(request)
        return HttpResponseRedirect(reverse_lazy('users_app:login'))
