from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):

    # is_staff => permite o no acceder al administrador
    # is_superuser => permisos de superusuario
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        # Guardando el usuario y espeficicando en que BD se debe almacenar
        user.save(using=self.db)
        return user

    # Sobreescribiendo la funcion que permite crear super usuarios
    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)

    # Sobreescribiendo la funcion que permite crear usuarios
    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def cod_registro_validate(self, id_user, cod_registro):
        # Consultando en la bd si el usuario y codigo de registro existen
        if self.filter(id=id_user, cod_registro=cod_registro).exists():
            return True
        return False
