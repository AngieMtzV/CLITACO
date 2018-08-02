from django.conf.urls import url,include
#from django.contrib.auth.decorators import login_required
from views import CajaClitaco

urlpatterns = [
    url(r'^caja', CajaClitaco.as_view(),   name='caja'),

    

]
    
