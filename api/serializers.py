from rest_framework import serializers
from inv.models import Producto
from bases.models import Notificacion
from usr.models import Profile

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Producto
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


