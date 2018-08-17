from django.conf.urls import url,include
from views import material_view, ListaMaterial


urlpatterns = [
    url(r'^material/', material_view, name='materialnuevo_form'),
    url(r'^lista/material', ListaMaterial.as_view(), name='material_lista'),
   
]