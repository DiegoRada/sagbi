from django.db import models

class Paises(models.Model):
	
	nombre_pais = models.CharField(max_length=50,unique=True)
	estatus_pais = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre_pais

	def __str__(self):
		return self.nombre_pais

class Directores(models.Model):
	
	nombre_director = models.CharField(max_length=50)
	estatus_director = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre_director

	def __str__(self):
		return self.nombre_director

class Peliculas(models.Model):
	
	titulo_original = models.CharField(max_length=150, db_index=True)
	titulo_traducido = models.CharField(max_length=150,null=True)
	anio = models.PositiveIntegerField()
	duracion = models.CharField(max_length=10)
	pais = models.ForeignKey(Paises)
	director = models.ForeignKey(Directores)
	guion = models.CharField(max_length=255,null=True)
	fotografia = models.CharField(max_length=255,null=True)
	reparto = models.CharField(max_length=255,null=True)
	productora = models.CharField(max_length=150,null=True)
	sinopsis = models.TextField(max_length=800,null=True)
	criticas = models.TextField(max_length=1300,null=True)
	
	pelicula_digital = models.FileField(upload_to='peliculas/')
	pelicula_afiche = models.FileField(upload_to='peliculas/',null=True)
	subtitulo = models.FileField(upload_to='peliculas/',null=True)
	pelicula_ficha = models.FileField(upload_to='peliculas/',null=True)

	def __unicode__(self):
		return self.titulo_original

	def __str__(self):
		return self.titulo_original

class Valoracion_peliculas(models.Model):
	
	id_pelicula = models.ForeignKey(Peliculas)
	valoracion_pelicula = models.PositiveIntegerField()

	def __unicode__(self):
		return "%s %s" % (self.peliculas.titulo_original, self.valoracion_pelicula)

	def __str__(self):
		return "%s %s" % (self.peliculas.titulo_original, self.valoracion_pelicula)


class Autores(models.Model):
	
	nombre_autor = models.CharField(max_length=50)
	estatus_autor = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre_autor

	def __str__(self):
		return self.nombre_autor

class Libros(models.Model):
	
	titulo_libro = models.CharField(max_length=150, db_index=True)
	autor = models.ForeignKey(Autores)
	isbn = models.CharField(max_length=100,null=True)
	edicion = models.CharField(max_length=100,null=True)
	publicacion = models.CharField(max_length=100,null=True)
	descripcion = models.TextField(max_length=1000,null=True)
	
	libro_digital = models.FileField(upload_to='libros/')
	libro_afiche = models.FileField(upload_to='libros/',null=True)
	libro_ficha = models.FileField(upload_to='libros/',null=True)


	def __unicode__(self):
		return self.titulo_libro

	def __str__(self):
		return self.titulo_libro

class Valoracion_libros(models.Model):
	
	id_libro = models.ForeignKey(Libros)
	valoracion_libro = models.PositiveIntegerField()

	def __unicode__(self):
		return "%s %s" % (self.libros.titulo_libro, self.valoracion_libro)

	def __str__(self):
		return "%s %s" % (self.libros.titulo_libro, self.valoracion_libro)