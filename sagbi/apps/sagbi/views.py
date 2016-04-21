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
	mensaje = ''
	if request.method == 'POST':
		pelicula_c = Peliculas.objects.filter(titulo_original=request.POST['titulo_original'], anio=request.POST['anio'])
		if len(pelicula_c) > 0:
			mensaje = 'La Película que ha intentado cargar ya esta registrada, por favor verifique sus datos.'
		else:
			pelicula = Peliculas()
			pelicula.titulo_original = request.POST['titulo_original']
			pelicula.titulo_traducido = request.POST['titulo_traducido']
			pelicula.anio = request.POST['anio']
			pelicula.duracion = request.POST['duracion']

			pais = get_object_or_404(Paises, pk=request.POST['pais'])
			pelicula.pais = pais

			director = get_object_or_404(Directores, pk=request.POST['director'])
			pelicula.director = director

			pelicula.guion = request.POST['guion']
			pelicula.fotografia = request.POST['fotografia']
			pelicula.reparto = request.POST['reparto']
			pelicula.productora = request.POST['productora']
			pelicula.sinopsis = request.POST['sinopsis']
			pelicula.criticas = request.POST['criticas']
			pelicula.pelicula_digital = request.FILES['pelicula_digital']
			pelicula.pelicula_afiche = request.FILES.get('pelicula_afiche', '')
			pelicula.subtitulo = request.FILES.get('subtitulo', '')
			pelicula.pelicula_ficha = request.FILES.get('pelicula_ficha', '')

			pelicula.save()

	peliculas = Peliculas.objects.order_by("-id")
	paises = Paises.objects.order_by("-id")
	directores = Directores.objects.order_by("-id")
	return render(request, 'panel/agregar_pelicula.html',{'peliculas' : peliculas, 'paises' : paises, 'directores' : directores, 'mensaje' : mensaje})

@login_required()
def modificar_pelicula(request, pelicula_id):
	pelicula = get_object_or_404(Peliculas, pk=pelicula_id)
	paises = Paises.objects.order_by("-id")
	directores = Directores.objects.order_by("-id")

	return render(request, 'panel/modificar_pelicula.html',{'pelicula' : pelicula, 'paises' : paises, 'directores' : directores})

@login_required()
def guardar_modificar_pelicula(request):
	if request.method == 'POST':
		mensaje = ''
		if 'modificar_pelicula_datos' in request.POST:
			pelicula_c = Peliculas.objects.filter(titulo_original=request.POST['titulo_original_modificar'], anio=request.POST['anio_modificar'])
			if len(pelicula_c) > 1:
				mensaje = 'La Película que ha intentado modificar esta duplicada, por favor verifique sus datos.'
			else:
				pelicula = get_object_or_404(Peliculas, pk=request.POST['pelicula_id'])
				pelicula_respaldo = get_object_or_404(Peliculas, pk=request.POST['pelicula_id'])
				pelicula.titulo_original = request.POST['titulo_original_modificar']
				pelicula.titulo_traducido = request.POST['titulo_traducido_modificar']
				pelicula.anio = request.POST['anio_modificar']
				pelicula.duracion = request.POST['duracion_modificar']

				pais = get_object_or_404(Paises, pk=request.POST['pais_modificar'])
				pelicula.pais = pais

				director = get_object_or_404(Directores, pk=request.POST['director_modificar'])
				pelicula.director = director

				pelicula.guion = request.POST['guion_modificar']
				pelicula.fotografia = request.POST['fotografia_modificar']
				pelicula.reparto = request.POST['reparto_modificar']
				pelicula.productora = request.POST['productora_modificar']
				pelicula.sinopsis = request.POST['sinopsis_modificar']
				pelicula.criticas = request.POST['criticas_modificar']

				pelicula.save()

				mensaje = 'La Película ha sido modificada exitosamente.'

				pelicula_c2 = Peliculas.objects.filter(titulo_original=request.POST['titulo_original_modificar'], anio=request.POST['anio_modificar'])
				if len(pelicula_c2) > 1:
					pelicula.delete()
					pelicula_respaldo.save()

					mensaje = 'La Película que ha intentado modificar esta duplicada, por favor verifique sus datos.'
				
		if 'modificar_pelicula_archivos' in request.POST:
			pelicula_archivo = get_object_or_404(Peliculas, pk=request.POST['pelicula_id'])

			if request.FILES.get('pelicula_digital_modificar', ''):
				pelicula_archivo.pelicula_digital = request.FILES.get('pelicula_digital_modificar', '')
			
			if request.FILES.get('pelicula_afiche_modificar', ''):
				pelicula_archivo.pelicula_afiche = request.FILES.get('pelicula_afiche_modificar', '')
			
			if request.FILES.get('subtitulo_modificar', ''):
				pelicula_archivo.subtitulo = request.FILES.get('subtitulo_modificar', '')
			
			if request.FILES.get('pelicula_ficha_modificar', ''):
				pelicula_archivo.pelicula_ficha = request.FILES.get('pelicula_ficha_modificar', '')			

			pelicula_archivo.save()

			mensaje = 'La Película ha sido modificada exitosamente.'

		peliculas = Peliculas.objects.order_by("-id")
		paises = Paises.objects.order_by("-id")
		directores = Directores.objects.order_by("-id")
		return render(request, 'panel/agregar_pelicula.html',{'peliculas' : peliculas, 'paises' : paises, 'directores' : directores, 'mensaje' : mensaje})

	else:
		return redirect('/inicio-sesion')


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
	mensaje = ''
	if request.method == 'POST':
		libro_c = Libros.objects.filter(isbn=request.POST['isbn'])
		if len(libro_c) > 0:
			mensaje = 'El ISBN del libro que ha intentado cargar ya esta registrado, por favor verifique sus datos.'
		else:
			libro = Libros()
			libro.titulo_libro = request.POST['titulo_libro']
			autor = get_object_or_404(Autores, pk=request.POST['autor'])
			libro.autor = autor
			libro.isbn = request.POST['isbn']
			libro.edicion = request.POST['edicion']
			libro.publicacion = request.POST['publicacion']
			libro.descripcion = request.POST['descripcion']

			libro.libro_digital = request.FILES['libro_digital']
			libro.libro_afiche = request.FILES.get('libro_afiche', '')
			libro.libro_ficha = request.FILES.get('libro_ficha', '')

			libro.save()

	autores = Autores.objects.order_by("-id")
	libros = Libros.objects.order_by("-id")
	return render(request, 'panel/agregar_libro.html',{'libros' : libros, 'autores' : autores, 'mensaje' : mensaje})

@login_required()
def modificar_libro(request, libro_id):
	libro = get_object_or_404(Libros, pk=libro_id)
	autores = Autores.objects.order_by("-id")
	return render(request, 'panel/modificar_libro.html',{'libro' : libro, 'autores' : autores})

@login_required()
def guardar_modificar_libro(request):
	if request.method == 'POST':
		mensaje = ''
		if 'modificar_libro_datos' in request.POST:
			libro_c = Libros.objects.filter(isbn=request.POST['isbn_modificar'])
			if len(libro_c) > 1:
				mensaje = 'El ISBN del libro que ha intentado modificar esta duplicado, por favor verifique sus datos.'
			else:
				libro = get_object_or_404(Libros, pk=request.POST['libro_id'])
				libro_respaldo = get_object_or_404(Libros, pk=request.POST['libro_id'])

				libro.titulo_libro = request.POST['titulo_libro_modificar']
				autor = get_object_or_404(Autores, pk=request.POST['autor_modificar'])
				libro.autor = autor
				libro.isbn = request.POST['isbn_modificar']
				libro.edicion = request.POST['edicion_modificar']
				libro.publicacion = request.POST['publicacion_modificar']
				libro.descripcion = request.POST['descripcion_modificar']

				libro.save()

				mensaje = 'El libro ha sido modificado exitosamente.'

				libro_c2 = Libros.objects.filter(isbn=request.POST['isbn_modificar'])
				if len(libro_c2) > 1:
					libro.delete()
					libro_respaldo.save()

					mensaje = 'El ISBN del libro que ha intentado modificar esta duplicado, por favor verifique sus datos.'
				
		if 'modificar_libro_archivos' in request.POST:
			libro_archivo = get_object_or_404(Libros, pk=request.POST['libro_id'])

			if request.FILES.get('libro_digital_modificar', ''):
				libro_archivo.libro_digital = request.FILES.get('libro_digital_modificar', '')
			
			if request.FILES.get('libro_afiche_modificar', ''):
				libro_archivo.libro_afiche = request.FILES.get('libro_afiche_modificar', '')
			
			if request.FILES.get('libro_ficha_modificar', ''):
				libro_archivo.libro_ficha = request.FILES.get('libro_ficha_modificar', '')			

			libro_archivo.save()

			mensaje = 'El libro ha sido modificado exitosamente.'

		autores = Autores.objects.order_by("-id")
		libros = Libros.objects.order_by("-id")
		return render(request, 'panel/agregar_libro.html',{'libros' : libros, 'autores' : autores, 'mensaje' : mensaje})

	else:
		return redirect('/inicio-sesion')