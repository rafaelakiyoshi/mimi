"""milena URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^start/$', views.start, name='start'),
    url(r'^start/dica$', views.startDica, name='startDica'),
    url(r'^tword/$', views.tword, name='tword'),
    url(r'^tword/dica$', views.twordDica, name='twordDica'),
    url(r'^threerd/$', views.threerd, name='threerd'),
    url(r'^threerd/dica$', views.threerdDica, name='threerdDica'),
    url(r'^fourrd/$', views.fourrd, name='fourrd'),
    url(r'^fourrd/dica$', views.fourrdDica, name='fourrdDica'),
    url(r'^fiverd/$', views.fiverd, name='fiverd'),
    url(r'^fiverd/dica$', views.fiverdDica, name='fiverdDica'),
    url(r'^sixrd/$', views.sixrd, name='sixrd'),
    url(r'^sixrd/dica$', views.sixrdDica, name='sixrdDica'),
]
