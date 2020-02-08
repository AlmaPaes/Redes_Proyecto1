# redes/urls.py

from django.conf.urls import url
from redes import views
#from django.urls import path
#from .views import redirect_view

# SET THE NAMESPACE!
app_name = 'redes'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^perritos/$',views.perritos,name='perritos'),
]
