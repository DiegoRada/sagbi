#encoding:utf-8
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'index.html')

def peliculas(request):
	return render(request, 'peliculas.html')

def detalles_pelicula(request):
	return render(request, 'detalles_pelicula.html')

def detalles_plus_pelicula(request):
	return render(request, 'detalles_plus_pelicula.html')

def libros(request):
	return render(request, 'libros.html')

def detalles_libro(request):
	return render(request, 'detalles_libro.html')

def detalles_plus_libro(request):
	return render(request, 'detalles_plus_libro.html')

def busqueda_material(request):
	return render(request, 'busqueda_material.html')


# VIEWS PANEL

@login_required()
def inicio(request):
	return render(request, 'panel/inicio.html')


@login_required()
def agregar_pais(request):
	if request.is_ajax():
		pais_c = Paises.objects.filter(nombre_pais=request.POST['pais'])
		if len(pais_c) > 0:
			return HttpResponse('<div class="alert alert-danger text-center" role="alert"><b>Este país ya esta registrado, por favor verifique sus datos.</b></div>')				
		else:
			pais = Paises.objects.create(nombre_pais=request.POST['pais'])
			return HttpResponse('<div class="alert alert-success text-center" role="alert"><b>País registrado exitosamente.</b></div>')
	else:
		paises = Paises.objects.order_by("-id")
		return render(request, 'panel/agregar_pais.html',{'paises' : paises})

@login_required()
def modificar_pais(request, pais_id):
	pais = get_object_or_404(Paises, pk=pais_id)

	return render(request, 'panel/modificar_pais.html',{'pais' : pais})

@login_required()
def guardar_modificar_pais(request):
	if request.is_ajax():
		pais_c = Paises.objects.filter(nombre_pais=request.POST['pais'])
		if len(pais_c) > 0:
			return HttpResponse('<div class="alert alert-danger text-center" role="alert"><b>Este país ya esta registrado, por favor verifique sus datos.</b></div>')				
		else:
			pais = get_object_or_404(Paises, pk=request.POST['pais_id'])
			pais.nombre_pais = request.POST['pais']
			pais.save()

			return HttpResponse('<div class="alert alert-success text-center" role="alert"><b>País modificado exitosamente.</b></div>')
	else:
		return redirect('/inicio-sesion')


@login_required()
def agregar_director(request):
	if request.is_ajax():
		director_c = Directores.objects.filter(nombre_director=request.POST['director'])
		if len(director_c) > 0:
			return HttpResponse('<div class="alert alert-danger text-center" role="alert"><b>Este director ya esta registrado, por favor verifique sus datos.</b></div>')				
		else:
			director = Directores.objects.create(nombre_director=request.POST['director'])
			return HttpResponse('<div class="alert alert-success text-center" role="alert"><b>Director registrado exitosamente.</b></div>')
	else:
		directores = Directores.objects.order_by("-id")
		return render(request, 'panel/agregar_director.html',{'directores' : directores})

@login_required()
def modificar_director(request, director_id):
	director = get_object_or_404(Directores, pk=director_id)

	return render(request, 'panel/modificar_director.html',{'director' : director})

@login_required()
def guardar_modificar_director(request):
	if request.is_ajax():
		director_c = Directores.objects.filter(nombre_director=request.POST['director'])
		if len(director_c) > 0:
			return HttpResponse('<div class="alert alert-danger text-center" role="alert"><b>Este director ya esta registrado, por favor verifique sus datos.</b></div>')				
		else:
			director = get_object_or_404(Directores, pk=request.POST['director_id'])
			director.nombre_director = request.POST['director']
			director.save()

			return HttpResponse('<div class="alert alert-success text-center" role="alert"><b>Director modificado exitosamente.</b></div>')
	else:
		return redirect('/inicio-sesion')


@login_required()
def agregar_pelicula(request):
	if request.is_ajax():
		director_c = Directores.objects.filter(nombre_director=request.POST['director'])
		if len(director_c) > 0:
			return HttpResponse('<div class="alert alert-danger text-center" role="alert"><b>Este director ya esta registrado, por favor verifique sus datos.</b></div>')				
		else:
			director = Directores.objects.create(nombre_director=request.POST['director'])
			return HttpResponse('<div class="alert alert-success text-center" role="alert"><b>Director registrado exitosamente.</b></div>')
	else:
		peliculas = Peliculas.objects.order_by("-id")
		paises = Paises.objects.order_by("-id")
		directores = Directores.objects.order_by("-id")
		return render(request, 'panel/agregar_pelicula.html',{'peliculas' : peliculas, 'paises' : paises, 'directores' : directores})


@login_required()
def agregar_autor(request):
	if request.is_ajax():
		autor_c = Autores.objects.filter(nombre_autor=request.POST['autor'])
		if len(autor_c) > 0:
			return HttpResponse('<div class="alert alert-danger text-center" role="alert"><b>Este autor ya esta registrado, por favor verifique sus datos.</b></div>')				
		else:
			autor = Autores.objects.create(nombre_autor=request.POST['autor'])
			return HttpResponse('<div class="alert alert-success text-center" role="alert"><b>Autor registrado exitosamente.</b></div>')
	else:
		autores = Autores.objects.order_by("-id")
		return render(request, 'panel/agregar_autor.html',{'autores' : autores})

@login_required()
def modificar_autor(request, autor_id):
	autor = get_object_or_404(Autores, pk=autor_id)

	return render(request, 'panel/modificar_autor.html',{'autor' : autor})

@login_required()
def guardar_modificar_autor(request):
	if request.is_ajax():
		autor_c = Autores.objects.filter(nombre_autor=request.POST['autor'])
		if len(autor_c) > 0:
			return HttpResponse('<div class="alert alert-danger text-center" role="alert"><b>Este autor ya esta registrado, por favor verifique sus datos.</b></div>')				
		else:
			autor = get_object_or_404(Autores, pk=request.POST['autor_id'])
			autor.nombre_autor = request.POST['autor']
			autor.save()

			return HttpResponse('<div class="alert alert-success text-center" role="alert"><b>Autor modificado exitosamente.</b></div>')
	else:
		return redirect('/inicio-sesion')


@login_required()
def agregar_libro(request):
	return render(request, 'panel/agregar_libro.html')