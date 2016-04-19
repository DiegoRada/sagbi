from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('apps.users.urls', namespace="users_app")),
	url(r'^',include('apps.sagbi.urls', namespace="sagbi_app")),
]