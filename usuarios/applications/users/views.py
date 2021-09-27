from django.core.mail import send_mail

from django.views.generic.edit import (FormView, View)
from .forms import UserRegiterForm, UserLoginForm, UpdatePasswordUserForm, VerificationdUserForm
from .models import User
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .functions import code_generator
from django.conf import settings

# Auth Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


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
        # Generando el codigo aleatorio
        cod_registro = code_generator(size=6)

        # Creando con la funcion definida en el manager
        user_created = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero'],
            cod_registro=cod_registro
        )

        # Enviar el codigo al email del usuario
        asunto = f"Confirmacion de Email - {form.cleaned_data['nombres']}"
        mensaje = 'Codigo de verificacion: ' + cod_registro
        email_remitente = settings.EMAIL_HOST_USER

        send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email'], ])

        # Redirigir a pantalla de validacion ya no al constructr de la misma clase

        # return super(UserRegisterView, self).form_valid(form)
        return HttpResponseRedirect(reverse_lazy('users_app:confirmation_code', kwargs={'pk': user_created.id}))


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


# LoginRequiredMixin => añade mixin de capa de seguridad de login
class UpdatePasswordUserView(LoginRequiredMixin, FormView):
    # Epceificando el html a rendeirzar
    template_name = 'users/update_password.html'
    # Especificando el formulario
    form_class = UpdatePasswordUserForm
    # Url de redireccion cuando complete
    success_url = reverse_lazy('users_app:login')

    # En caso que no este autenticado se redireccionara se define la redireccion
    login_url = reverse_lazy('users_app:login')

    # Funcion que escucha el REQUEST del view
    def form_valid(self, form):
        # Accediendo al usuario atutenticado
        usuario = self.request.user
        user_authenticate = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1'],
        )
        if user_authenticate:
            new_password = form.cleaned_data['password2']
            # actualizando el usuario actual con la contraseña encriptada
            usuario.set_password(new_password)
            usuario.save()

        # Cerrando la sesion por seguridad
        logout(self.request)

        return super(UpdatePasswordUserView, self).form_valid(form)


class CodeVerificationUserView(FormView):
    # Epceificando el html a rendeirzar
    template_name = 'users/verification_code.html'
    # Especificando el formulario
    form_class = VerificationdUserForm
    # Url de redireccion cuando complete
    success_url = reverse_lazy('users_app:login')

    # Funcion que permite sobreescribir el contento de parametros por url para que se puedan enviar al formulario
    def get_form_kwargs(self):
        kwargs = super(CodeVerificationUserView, self).get_form_kwargs()
        # añadimos al contexto global de kwargs para poder acceder desde el formulario
        kwargs.update({'pk': self.kwargs['pk']})
        return kwargs

    # Funcion que escucha el REQUEST del view
    def form_valid(self, form):
        # Recuperando el usuario por el id pasado por parametro, y actualizando su estado
        User.objects.filter(id=self.kwargs['pk']).update(is_active=True)

        return super(CodeVerificationUserView, self).form_valid(form)
