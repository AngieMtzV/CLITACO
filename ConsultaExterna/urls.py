from django.conf.urls import url,include,handler500
from views import ValoracionInicialCreate, TablaEvolucion, ListaConsultaExterna, CuadroAvanceRapido, DetallesConsultaExterna, ValoracionEdit,ReferenciaContraReferencia, DetallesReferencia,view404referencia,valoracion_edit
urlpatterns = [
    url(r'^consultaexterna/valoracion', ValoracionInicialCreate.as_view(), name='valoracion_inicial'),
    url(r'^consultaexterna/editar/(?P<pk>\d+)/$', valoracion_edit, name='valoracion_edit'), 
    url(r'^consultaexterna/evolucion/(?P<pk>\d+)/evolucion$', TablaEvolucion.as_view(), name='table_evolucion'),#Agregar Campo de Diagnostico
    url(r'^consultaexterna/lista', ListaConsultaExterna.as_view(), name='listas_externa'),
    url(r'^consultaexterna/avanceRapido', CuadroAvanceRapido.as_view(), name='avance_rapido'), #Cambiarlo por un DetailView
    url(r'^consultaexterna/detalles/(?P<pk>\d+)/$', DetallesConsultaExterna.as_view(), name='avance_rapido_detalles'),
    url(r'^consultaexterna/referencia/(?P<pk>\d+)/$', ReferenciaContraReferencia.as_view(), name='referencia_create'),
    url(r'^consultaexterna/detallesRef/(?P<pk>\d+)/$', DetallesReferencia.as_view(), name='detalles_ref'),
    url(r'^consultaexterna/detallesRef/$',view404referencia, name='404_referencia'),
    

    #Constancia y Certificado Medico agregarlos para que generen un pdf

]
handler500 = 'accounts.views.page_not_found' 