"""project URL Configuration

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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shanu.url')),
    path('about',include('shanu.url')),
    path('contact',include('shanu.url')),
    path('services',include('shanu.url')),
    path('services2',include('shanu.url')),
    path('services',include('shanu.url')),
    path('jaipur',include('shanu.url')),
    path('jodh',include('shanu.url')),
    path('jaisal',include('shanu.url')),
    path('pali',include('shanu.url')),
    path('udaipur',include('shanu.url')),
    path('kota',include('shanu.url')),
    path('bikaner',include('shanu.url')),
    path('bharatpur',include('shanu.url')),
    path('alwar',include('shanu.url')),
    path('weather',include('shanu.url')),
]
