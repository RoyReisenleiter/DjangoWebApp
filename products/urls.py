from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('new', views.new)
]




#http://127.0.0.1:8000/products/

#django-admin startproject pyshop
#python manage.py runserver
#python manage.py startapp products

#migrate database
#python manage.py makemigrations
#python manage.py migrate

#admin
#python manage.py createsuperuser