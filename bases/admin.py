from django.contrib import admin
from .models import Notificacion, Provincia, Codigo_Postal

# Register your models here.

admin.site.register(Notificacion)
admin.site.register(Provincia)
admin.site.register(Codigo_Postal)