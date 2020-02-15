from django.conf import settings    # <--------
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('menu/', include('menu.urls')),
    path('reservation/', include('reservation.urls')),
    # path('accounts/', include('django.contrib.auth.urls'))
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LoginView.as_view(), name='logout'),
]

if settings.DEBUG:                  # <--------
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls)),
    ] + urlpatterns