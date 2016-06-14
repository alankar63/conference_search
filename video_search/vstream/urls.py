from django.conf.urls import url
from . import views

# will use it later 
urlpatterns = [
    url(r'^$', views.fill, name='data_fill'),
        ]
