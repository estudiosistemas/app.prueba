from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views
from api.views import Login,Logout

from bases.views import Home, HomeSinPrivilegios, NotificacionView, notificacion_leer, NotificacionNew, notificacion_read
from .views import CustomAuthToken


urlpatterns = [
    path('',Home.as_view(), name='home'),
    #path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='base/login.html'), name='logout'),
    path('login/',Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('api_generate_token/', CustomAuthToken.as_view(), name='api_generate_token'),
    
    path('sin_privilegios/',HomeSinPrivilegios.as_view(), name='sin_privilegios'),

    path('notify/', NotificacionView.as_view(), name='notificacion_list'),
    path('notify/new', NotificacionNew.as_view(), name='notificacion_new'),
    path('notify/leer/<int:id>', notificacion_leer, name='notificacion_leer'),
    path('notify/read/<int:id>', notificacion_read, name='notificacion_read'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
