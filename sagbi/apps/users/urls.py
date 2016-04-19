from django.conf.urls import patterns, url

urlpatterns = patterns('',
		url(r'^inicio-sesion/$', 'apps.users.views.inicio_sesion', name="inicio_sesion"),
		url(r'^cierre-sesion/$', 'apps.users.views.cierre_sesion', name="cierre_sesion"),
		url(r'^perfil/$', 'apps.users.views.perfil', name="perfil"),
		url(r'^pre-registro/$', 'apps.users.views.pre_registro', name="pre_registro"),
		url(r'^registro-usuario/$', 'apps.users.views.registro_usuario', name="registro_usuario"),
		url(r'^formulario-registro/(?P<id_user>[0-9]+)/$', 'apps.users.views.formulario_registro', name="formulario_registro"),
		url(r'^guardar-formulario-registro/$', 'apps.users.views.guardar_formulario_registro', name="guardar_formulario_registro"),
		url(r'^restablecer-password/$', 'apps.users.views.restablecer_password', name="restablecer_password"),							
	)
	