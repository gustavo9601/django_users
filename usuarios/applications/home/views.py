from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

# Create your views here.
from django.views.generic import (TemplateView)


class FechaMixin(object):
    # Funcion que define la data a enviar a las vistas en el contexto
    def get_context_data(self, **kwargs):
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.datetime.now
        return context


class TemplatePruebaMixin(FechaMixin, TemplateView):
    template_name = 'home/test_mixin.html'


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'

    # Al herededar de LoginRequiredMixin, se define login_url, para definir a donde se redirecciona si
    # no esta autenticado
    login_url = reverse_lazy('users_app:login')
