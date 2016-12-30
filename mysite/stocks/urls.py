from django.conf.urls import url,include
from . import views

urlpatterns = [
   
   url(r'^stocks/$', views.stockslist, name = 'stockslist'),
]