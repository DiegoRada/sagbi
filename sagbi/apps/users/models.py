from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager, models.Manager):

	def _create_user(self, cedula, nombre, apellido, email, password, is_staff,
				is_superuser, **extra_fields):

		email = self.normalize_email(email)
		if not email:
			raise ValueError('El email debe ser obligatorio')
		user = self.model(cedula = cedula, nombre = nombre, apellido = apellido, email = email, is_active=True,
				is_staff = is_staff, is_superuser = is_superuser, **extra_fields)
		user.set_password(password)
		user.save( using = self._db)
		return user

	def create_user(self, cedula, nombre, apellido, email, password=None, **extra_fields):
		return self._create_user(cedula, nombre, apellido, email, password, False,
				False, **extra_fields)

	def create_superuser(self, cedula, nombre, apellido, email, password=None, **extra_fields):
		return self._create_user(cedula, nombre, apellido, email, password, True,
				True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

	cedula = models.PositiveIntegerField(unique=True)	
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	email = models.EmailField(max_length=50, null=True)

	objects = UserManager()

	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)

	USERNAME_FIELD = 'cedula'
	REQUIRED_FIELDS = ['nombre','apellido','email']

# HACER QUE DEVUELVA EL OBJETO COMPLETO

	def __unicode__(self):
		return self.nombre + " " + self.apellido

	def __str__(self):
		return self.nombre + " " + self.apellido

	def get_short_name(self):
		return self.nombre