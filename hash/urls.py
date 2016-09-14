from django.conf.urls import url

from hash.views import Hashing, HashingLogin, HashingInit, HashLogout

urlpatterns = [
    url(r'^hash/$', Hashing.as_view(), name='hashing'),
    url(r'^hashLogin/$', HashingLogin.as_view(), name='hashingLogin'),
    url(r'^hashWelcome/$', HashingInit.as_view(), name='hashWelcome'),
    url(r'^hashBye/$', HashLogout.as_view(), name='hashLogout'),

]