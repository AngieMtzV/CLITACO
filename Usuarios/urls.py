from django.conf.urls import url,include
from views import docente_Medico

urlpatterns = [
    url(r'^docente/index', docente_Medico, name='docente_index'),
    url(r'^medico/index', docente_Medico, name='medico_index'),
    
   

]
