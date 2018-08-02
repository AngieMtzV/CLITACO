from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required
from views import nueva_historia_clinica, historia_clinica_controlado_edit,  nueva_historia_clinica_controlada, ListasHistoriasPorUser, ListasHistorias, Plan_TratamientoHC,Plan_EjecucionHC , nueva_historia_clinica_integral, historia_clinica_edit

urlpatterns = [
    url(r'^nuevahistoriaclinica/urgencia', login_required(nueva_historia_clinica),  name='historiaClinica_Form'),
    url(r'^urgencia/editar/(?P<pk>\d+)/$',  historia_clinica_edit,  name='editar_urgencia'),
    url(r'^nuevahistoriaclinica/controlada', login_required(nueva_historia_clinica_controlada),  name='historiaClinicaControlada_Form'),
    url(r'^controlada/editar/(?P<pk>\d+)/$',  historia_clinica_controlado_edit,  name='editar_controlado'),
    url(r'^nuevahistoriaclinica/integral',login_required( nueva_historia_clinica_integral),  name='historiaIntegral'),
    url(r'^listado/historiasClinicas', login_required(ListasHistoriasPorUser.as_view()),  name='listas'),
    url(r'^historiaClinica/plantratamiento', login_required(Plan_TratamientoHC.as_view()),  name='plan-tratamiento'),
    url(r'^historiaClinica/planejecucion', login_required(Plan_EjecucionHC.as_view()),  name='plan-ejecucion'),
    

]
    
