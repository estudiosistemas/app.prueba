from rest_framework import serializers
from inv.models import Producto
from bases.models import Notificacion

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Producto
        fields='__all__'


class NotificacionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Notificacion
        fields='__all__'
        depth = 1

