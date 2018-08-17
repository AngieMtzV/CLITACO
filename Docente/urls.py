from django.conf.urls import url,include
from views import AlumnoSeguimiento

urlpatterns = [
    url(r'^docente/seguimiento',AlumnoSeguimiento.as_view(), name='seguimiento_alumnos'),
   
    #url(r'^docente/alumnos',Lista_Alumnos, name='tabla_alumnos')
   

]
