from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='inicio'),
    path('mixin/', views.TemplatePruebaMixin.as_view(), name='mixin'),
]
