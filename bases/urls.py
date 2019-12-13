from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views
from api.views import Login,Logout

from bases.views import Home, HomeSinPrivilegios, NotificacionView, notificacion_leer, NotificacionNew, notificacion_read,  ProvinciasView, ProvinciaNew, ProvinciaEdit, provincia_inactivar
from .views import CustomAuthToken, Landing_Page


urlpatterns = [
    path('',Landing_Page.as_view(), name='index'),
    path('gtl/',Home.as_view(), name='home'),
    path('gtl/login/',Login.as_view(), name = 'login'),
    path('gtl/logout/', Logout.as_view(), name = 'logout'),
    path('gtl/api_generate_token/', CustomAuthToken.as_view(), name='api_generate_token'),
    
    path('gtl/sin_privilegios/',HomeSinPrivilegios.as_view(), name='sin_privilegios'),

    path('gtl/provincias/', ProvinciasView.as_view(), name='provincia_list'),
    path('gtl/provincias/new', ProvinciaNew.as_view(), name='provincia_new'),
    path('gtl/provincias/edit/<str:pk>', ProvinciaEdit.as_view(), name='provincia_edit'),
    path('gtl/provincias/inactivar/<str:id>', provincia_inactivar, name='provincia_inactivar'),

    path('gtl/notify/', NotificacionView.as_view(), name='notificacion_list'),
    path('gtl/notify/new', NotificacionNew.as_view(), name='notificacion_new'),
    path('gtl/notify/leer/<int:id>', notificacion_leer, name='notificacion_leer'),
    path('gtl/notify/read/<int:id>', notificacion_read, name='notificacion_read'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
