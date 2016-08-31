from django.conf.urls import url

from cripto.views import Criptonite

urlpatterns = [
    url(r'^', Criptonite.as_view(), name='inicio'),

]