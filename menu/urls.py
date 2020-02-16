from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='menu'),
    path('create/', views.MenuCreate.as_view() , name='menu_create'),
    path('<int:pk>/update/', views.MenuUpdate.as_view(), name='menu_update'),
    path('<int:pk>/delete/', views.MenuDelete.as_view(), name='menu_delete'),

]