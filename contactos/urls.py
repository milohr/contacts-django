from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^detalle/(?P<telefono>\w{0,50})/$', views.detalles),
    url(r'^agregar', views.agregar, name='agregar'),
    url(r'^buscar/$', views.buscar),

   

    ]
