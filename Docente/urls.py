from django.conf.urls import url,include
from views import AlumnoSeguimiento,ListAlumnosDocente, ListasHistorias, UrgenciaDetalle

urlpatterns = [
    url(r'^docente/seguimiento/(?P<pk>\d+)',AlumnoSeguimiento.as_view(), name='seguimiento_alumnos'),
    url(r'^docente/alumnos',ListAlumnosDocente.as_view(), name='tabla_alumnos'),
    url(r'^docente/historiasClinicas', ListasHistorias.as_view(),  name='historias_docente'),
    url(r'^docente/urgencia/(?P<pk>\d+)/$',UrgenciaDetalle.as_view(), name='detalle_urgencia'),

   
  
]
