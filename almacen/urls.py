from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'almacen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^materiales/$', 'Datos.views.index'),
    url(r'^materiales/(?P<material_id>\d+)/$', 'Datos.views.detalle'),
    url(r'^materiales/crear/$', 'Datos.views.area_crear', name="area_crear"),

)
