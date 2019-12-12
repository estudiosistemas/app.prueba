from rest_framework import serializers
from inv.models import Producto
from fac.models import Cliente
from bases.models import Notificacion, Provincia
from usr.models import Profile


class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Provincia
        fields=['codigo','nombre', 'estado']


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Producto
        fields='__all__'


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model=Cliente
        fields='__all__'



class NotificacionSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField('get_avatar')
    
    class Meta:
        model=Notificacion
        fields=('id','fc','uc','asunto','mensaje','user_destino', 'avatar')
        depth = 1

    def get_avatar(self, notificacion):
        avatar = notificacion.uc.profile.image.url
        return avatar


