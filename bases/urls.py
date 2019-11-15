from django.urls import path
from django.contrib.auth import views as auth_views

from bases.views import Home, HomeSinPrivilegios, NotificacionView, notificacion_leer, NotificacionNew, notificacion_read


urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='base/login.html'), name='logout'),
    path('sin_privilegios/',HomeSinPrivilegios.as_view(), name='sin_privilegios'),

    path('notify/', NotificacionView.as_view(), name='notificacion_list'),
    path('notify/new', NotificacionNew.as_view(), name='notificacion_new'),
    path('notify/leer/<int:id>', notificacion_leer, name='notificacion_leer'),
    path('notify/read/<int:id>', notificacion_read, name='notificacion_read'),
]
