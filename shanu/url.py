from django.contrib import admin
from django.urls import path
from shanu import views

urlpatterns = [
    path("", views.index, name='shanu'),
    path("about", views.about, name='shanu'),
    path("contact", views.contact, name='shanu'),
    path("services", views.services, name='shanu'),
    path("services2", views.services2, name='shanu'),
    path("services3", views.services3, name='shanu'),
    path("jaipur", views.jaipur, name='shanu'),
    path("jodh", views.jodh, name='shanu'),
    path("jaisal", views.jaisal, name='shanu'),
    path("pali", views.pali, name='shanu'),
    path("udaipur", views.udaipur, name='shanu'),
    path("kota", views.kota, name='shanu'),
    path("bikaner", views.bikaner, name='shanu'),
    path("bharatpur", views.bharatpur, name='shanu'),
    path("alwar", views.alwar, name='shanu'),
    path("weather", views.weather, name='shanu')
]