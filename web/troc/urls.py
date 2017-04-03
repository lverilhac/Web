from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^index2$', views.index2),
    url(r'^article/(\d+)/(\d+)$', views.view_troc),
    url(r'^register/$', views.register, name='register'),
    url(r'^connect/$', views.connect, name='connect'),  
]