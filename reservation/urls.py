from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.reservation_list, name='reservation_list'),
    path('list/<int:pk>/', views.reservation_details, name='reservation_details'),
    path('<int:pk>/edit/', views.ReservationEdition.as_view(), name='reservation_edition'),
    path('<int:pk>/delete/', views.ReservationDelete.as_view(), name='reservation_delete'),
    # path('create/', views.ReservationCreate.as_view(), name='reservation-create'),
    path('create/', views.reservation_create, name='reservation-create'),
    path('bar-availability/', views.bar_availability, name='bar_availability'),
    path('create/confirm/', views.ConfirmPage.as_view(), name='confirm')
]