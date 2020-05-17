from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='menu'),
    path('list/', views.menu_list, name='menu_list'),
    path('create/', views.menu_create, name='menu_create'),
    path('list/<int:pk>/', views.menu_details, name='menu_details'),
    path('<int:pk>/update/', views.MenuUpdate.as_view(), name='menu_update'),
    path('<int:pk>/delete/', views.MenuDelete.as_view(), name='menu_delete'),
    path('create/confirm/', views.ConfirmMenuPage.as_view(), name='menu_confirm'),
    # 
    path('create/new-category/', views.menu_category_create, name='menu_category_create'),
    path('list/<int:pk>/', views.menu_category_details, name='menu_category_details'),
    path('<int:pk>/delete/', views.MenuCategoryDelete.as_view(), name='menu_category_delete'),
    path('create/new-category/confirm/', views.ConfirmMenuCategoryPage.as_view(), name='menu_category_confirm'),
]