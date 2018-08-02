from django.conf.urls import url,include
from views import ValoracionInicialCreate, TablaEvolucion, ListaConsultaExterna, CuadroAvanceRapido, DetallesConsultaExterna, ValoracionEdit, DetallesReferencia

urlpatterns = [
    url(r'^consultaexterna/valoracion', ValoracionInicialCreate.as_view(), name='valoracion_inicial'),
    url(r'^consultaexterna/editar/(?P<pk>\d+)/$', ValoracionEdit.as_view(), name='valoracion_edit'), 
    url(r'^consultaexterna/evolucion/(?P<pk>\d+)/$', TablaEvolucion.as_view(), name='table_evolucion'),#Agregar Campo de Diagnostico
    url(r'^consultaexterna/lista', ListaConsultaExterna.as_view(), name='listas_externa'),
    url(r'^consultaexterna/avanceRapido', CuadroAvanceRapido.as_view(), name='avance_rapido'), #Cambiarlo por un DetailView
    url(r'^consultaexterna/detalles/(?P<pk>\d+)/$', DetallesConsultaExterna.as_view(), name='avance_rapido_detalles'),
    

    #Constancia y Certificado Medico agregarlos para que generen un pdf

]