from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


# Usamos la clase abstrcta propia de Dajngo
class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros')
    )

    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # Se especifica por que campo se podra acceder al dasmin dashboard
    USERNAME_FIELD = 'username'
    # Especifica los campos que seran requeridos por consola
    REQUIRED_FIELDS = ['email',]
    # Enlazando el manager del modelo
    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        db_table = 'users'
