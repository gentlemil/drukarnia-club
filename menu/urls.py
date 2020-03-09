from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='menu'),
    path('list/', views.menu_list, name='menu_list'),
    path('create/', views.menu_create, name='menu_create'),
    path('list/<int:pk>/', views.menu_details, name='menu_details'),
    path('<int:pk>/delete/', views.MenuDelete.as_view(), name='menu_delete'),
    path('create/confirm/', views.ConfirmMenuPage.as_view(), name='menu_confirm'),
]