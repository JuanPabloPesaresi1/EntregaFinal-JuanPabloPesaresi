from xml.dom.minidom import Document
from django import views
from django.conf import settings
from django.contrib import admin
from django.forms import Media
from django.urls import path,include
from my_site.views import *
from AppCoder import views
from django.conf.urls.static import *
from django.conf import settings


urlpatterns = [
    path('admin', admin.site.urls,name="admin"),
    path('', views.entrada),    
    #URLS DE LA APP
    path('appcoder/',include('AppCoder.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)