from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.reservation_list, name='reservation_list'),
    path('create/', views.reservation_create, name='reservation-create'),
    path('list/<int:pk>/', views.reservation_details, name='reservation_details'),
    path('<int:pk>/edit/', views.ReservationEdition.as_view(), name='reservation_edition'),
    path('<int:pk>/delete/', views.ReservationDelete.as_view(), name='reservation_delete'),
    # path('bar-availability/', views.bar_availability, name='bar_availability'),
    path('create/confirm/', views.ConfirmReservation.as_view(), name='confirm'),

]