from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from .views import profileUser, registerUser


urlpatterns = [
    path('perfil/', profileUser, name='perfil_usuario'),
    path('registrar/', registerUser, name='registrar_usuario'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
