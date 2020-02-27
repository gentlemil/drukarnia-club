from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.aboutUs, name='aboutUs'),
    path('oferta/', views.barRental, name='barrental'),

]
