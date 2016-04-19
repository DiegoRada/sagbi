#encoding:utf-8
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, is_password_usable, make_password
from django.http import HttpResponse
from django.core.mail import EmailMessage
import random


from django.db.models import Q

def inicio_sesion(request):

	if request.user.is_authenticated():
		return redirect('/inicio')

	mensaje = ''

	if request.method == "POST":

		cedula = request.POST['cedula']
		password = request.POST['password']

		user = authenticate(cedula = cedula, password = password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('/inicio')
		 	else:
		 		mensaje = 'Este usuario no esta activo, por favor contacte al administrador.'

		mensaje = 'Cedula y/o Clave incorrecta, por favor verifique sus datos.'	
	
	return render(request,'panel/inicio_sesion.html',{'mensaje' : mensaje})

@login_required()
def cierre_sesion(request):
	logout(request)
	return redirect('/')

@login_required()
def perfil(request):

	mensaje = ''
	mensaje2 = ''

	if request.method == "POST":
		if 'modificar_perfil' in request.POST:
			user = get_object_or_404(User, pk=request.POST['id_user'])
			user.cedula = request.POST['cedula']
			user.nombre = request.POST['nombre']
			user.apellido = request.POST['apellido']
			user.email = request.POST['email']

			user.save()

			mensaje = 'Su perfil se ha modificado exitosamente.'

		if 'cambiar_clave' in request.POST:
			user = get_object_or_404(User, pk=request.POST['id_user'])
			user.password = make_password(request.POST['password'])

			user.save()
			
			mensaje2 = 'Su clave se ha modificado exitosamente.'

	return render(request, 'panel/perfil.html',{'mensaje' : mensaje, 'mensaje2' : mensaje2})
	

@login_required()
def pre_registro(request):
	mensaje = ''
	mensaje2 = ''
	if request.method == "POST":
		user_c = User.objects.filter(cedula=request.POST['cedula'])
		if len(user_c) > 0:
			mensaje2 ='Este usuario ya esta registrado, por favor verifique sus datos.'			
		else:			
			user = User()
			user.cedula = request.POST['cedula']
			user.nombre = request.POST['nombre']
			user.apellido = request.POST['apellido']
			user.email = request.POST['email']

			user.save()

			mensaje = 'El usuario se ha registrado exitosamente.'

	return render(request, 'panel/pre_registro.html',{'mensaje' : mensaje, 'mensaje2' : mensaje2})

def registro_usuario(request):
	if request.is_ajax():
		user_c = User.objects.filter(cedula=request.POST['cedula'])
		if len(user_c)==0:			
			return HttpResponse('<div class="alert alert-danger text-center" role="alert"><b>Esta cedula no esta registrada en el sistema, por favor contacte al administrador.</b></div>')
		else:
			user = User.objects.get(cedula=request.POST['cedula'])

			if user.password != '':
			 	return HttpResponse('<div class="alert alert-danger text-center" role="alert"><b>El usuario con esta cedula ya esta registrado, por favor verifique sus datos.</b></div>')
			else:
				return HttpResponse('<p class="msg-azul text-left">Hola <b>%s</b> ya puedes registrarte.<button type="button" class="btn btn-md pull-right" data-toggle="modal" data-target="#formulario_registro" href="/formulario-registro/%s/"><b>Registrarme</b></button></p>' % (user.nombre, user.id))
	else:
		return redirect('/inicio-sesion')

def formulario_registro(request, id_user):

	user = get_object_or_404(User, pk=id_user)

	return render(request, 'panel/formulario_registro.html',{'user' : user})

def guardar_formulario_registro(request):

	if request.method == "POST":
		user = get_object_or_404(User, pk=request.POST['id_user'])
		user.cedula = request.POST['cedula']
		user.nombre = request.POST['nombre']
		user.apellido = request.POST['apellido']
		user.email = request.POST['email']
		user.password = make_password(request.POST['password'])

		user.save()

		return redirect('/inicio-sesion')

	else:
		return redirect('/inicio-sesion')

def restablecer_password(request):
	if request.is_ajax():
		user_c = User.objects.filter(email=request.POST['email'])
		if len(user_c)==0:			
			return HttpResponse('<div class="alert alert-danger text-center" role="alert"><b>Este correo electronico no esta registrado en el sistema, por favor verifique sus datos.</b></div>')
		else:
			user = User.objects.get(email=request.POST['email'])

			an = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
			su = len(an) - 1
			password_aleatorio = an[random.randint(0, su)] + an[random.randint(0, su)] + an[random.randint(0, su)] + an[random.randint(0, su)] + an[random.randint(0, su)] + an[random.randint(0, su)] + an[random.randint(0, su)] + an[random.randint(0, su)]

			user.password = make_password(password_aleatorio)
			user.save()

			asunto = 'Clave Restablecida - Sistema Automatizado de Gestion de Bibliotecas (SAGBI)'
			mensaje = """Su nueva clave temporal es: %s

Por favor inicie sesion en SAGBI y cambie su clave por una mas segura.""" %(password_aleatorio)
			remitente = 'sagbi.sistema@gmail.com'
			destinatario = [user.email]
			mail = EmailMessage(asunto, mensaje, remitente, destinatario)			

			if mail.send(fail_silently=False):
				return HttpResponse('<div class="alert alert-info text-center" role="alert"><b>Le hemos enviado un correo electronico con su nueva clave temporal.</b></div>')
			else:
				return HttpResponse('<div class="alert alert-danger text-center" role="alert"><b>Ha ocurrido un error durante el envio del correo electronico con su nueva clave temporal, por favor contacte al administrador.</b></div>')
	else:
		return redirect('/')