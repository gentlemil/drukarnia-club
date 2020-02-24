from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about-us/', views.aboutUs, name='aboutus'),
    path('bar-rental/', views.barRental, name='barrental'),

]
