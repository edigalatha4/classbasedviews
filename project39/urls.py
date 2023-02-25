"""project39 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbv_djangoform/',fbv_djangoform,name='fbv_djangoform'),
    path('cbvdjangoform/',cbvdjangoform.as_view(),name='cbvdjangoform'),

    path('fbv_string/',fbv_string,name='fbv_string'),
    path('cbvstring/',cbvstring.as_view(),name='cbvstring'),


    path('fbv_htmlpage/',fbv_htmlpage,name='fbv_htmlpage'),
    path('cbvhtmlpage/',cbvhtmlpage.as_view(),name='cbvhtmlpage'),


    path('cbvtemplate/',TemplateView.as_view(template_name='cbvtemplate.html'),name='cbvtemplate'),
]
