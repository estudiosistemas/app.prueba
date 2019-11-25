from django.urls import path
from django.contrib.auth import views as auth_views

from bases.views import Home, HomeSinPrivilegios

from .views import ProductoList, ProductoDetalle, NotificacionList, NotificacionListWeb


urlpatterns = [
    path('v1/productos/',ProductoList.as_view(), name='producto_list'),
    path('v1/productos/<str:codigo>',ProductoDetalle.as_view(), name='producto_detalle'),
    path('v1/notify/<str:codigo>',NotificacionList.as_view(), name='notificacion_list'),
    path('v1/notifyWEB/<str:codigo>',NotificacionListWeb.as_view(), name='notificacion_listweb'),
]
