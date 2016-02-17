__author__ = 'jjh'
from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
admin.autodiscover()



"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

urlpatterns = patterns('',
                       url(r'^$', 'user_list', name='user_list'),
                       url(r'^api/(?P<pk>[0-9]+)/$', 'user_detail', name='user_detail'),
                       )

