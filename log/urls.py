"""log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from view import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexold),
    path('index/a', views.index, name='aa'),
    path('regist', views.register, name='ss'),
    path('view', views.login),
    path('show', views.show),
    path('main', views.main),
    path('login', views.logg),
    path('showmain', views.showmain),
    path('quit', views.quit),
    path('upfile', views.upfile),
    path('savefile', views.savefile),

]
