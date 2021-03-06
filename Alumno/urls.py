from django.conf.urls import url,include, handler404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout_then_login
from views import index, info_clitaco,RegistroAlumno, AlumnoPerfil, Perfil, view404perfil


urlpatterns = [
	url(r'^alumno/perfil/(?P<pk>\d+)/$',AlumnoPerfil.as_view(), name='alumno_perfil'),
	url(r'^alumno/perfil/crear',Perfil.as_view(), name='crear_perfil'),
	#url(r'^alumno/perfil/pdf2$',genera_pdf, name='pdf_alumno2'),
    url(r'^alumno/registro',RegistroAlumno.as_view(), name='alumno_form'),
    url(r'^alumno/index', login_required(index), name='alumno_index'),
    url(r'^acercade', info_clitaco, name='info'),
     url(r'^alumno/404/perfil/$',view404perfil, name='404_perfil'),
    
]

handler404 = 'accounts.views.page_not_found'
    