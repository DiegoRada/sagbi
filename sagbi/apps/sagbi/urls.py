from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'apps.sagbi.views.index', name="index"),
	url(r'^peliculas/$', 'apps.sagbi.views.peliculas', name="peliculas"),
	url(r'^detalles-pelicula/$', 'apps.sagbi.views.detalles_pelicula', name="detalles_pelicula"),
	url(r'^detalles-plus-pelicula/$', 'apps.sagbi.views.detalles_plus_pelicula', name="detalles_plus_pelicula"),
	url(r'^libros/$', 'apps.sagbi.views.libros', name="libros"),
	url(r'^detalles-libro/$', 'apps.sagbi.views.detalles_libro', name="detalles_libro"),
	url(r'^detalles-plus-libro/$', 'apps.sagbi.views.detalles_plus_libro', name="detalles_plus_libro"),
	url(r'^busqueda-material/$', 'apps.sagbi.views.busqueda_material', name="busqueda_material"),

	# URLS PANEL

	url(r'^inicio/$', 'apps.sagbi.views.inicio', name="inicio"),
	url(r'^agregar-pais/$', 'apps.sagbi.views.agregar_pais', name="agregar_pais"),
	url(r'^agregar-director/$', 'apps.sagbi.views.agregar_director', name="agregar_director"),
	url(r'^agregar-pelicula/$', 'apps.sagbi.views.agregar_pelicula', name="agregar_pelicula"),
	url(r'^agregar-autor/$', 'apps.sagbi.views.agregar_autor', name="agregar_autor"),
	url(r'^agregar-libro/$', 'apps.sagbi.views.agregar_libro', name="agregar_libro"),
	url(r'^modificar-pais/(?P<pais_id>[0-9]+)/$', 'apps.sagbi.views.modificar_pais', name="modificar_pais"),
	url(r'^guardar-modificar-pais/$', 'apps.sagbi.views.guardar_modificar_pais', name="guardar_modificar_pais"),
	url(r'^modificar-director/(?P<director_id>[0-9]+)/$', 'apps.sagbi.views.modificar_director', name="modificar_director"),
	url(r'^guardar-modificar-director/$', 'apps.sagbi.views.guardar_modificar_director', name="guardar_modificar_director"),
	url(r'^modificar-autor/(?P<autor_id>[0-9]+)/$', 'apps.sagbi.views.modificar_autor', name="modificar_autor"),
	url(r'^guardar-modificar-autor/$', 'apps.sagbi.views.guardar_modificar_autor', name="guardar_modificar_autor"),

)	