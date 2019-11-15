from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import ProductoSerializer, NotificacionSerializer
from inv.models import Producto
from bases.models import Notificacion

from django.db.models import Q 

class ProductoList(APIView):
    def get(self, request):
        prod = Producto.objects.all()
        data = ProductoSerializer(prod, many=True).data
        return Response(data)

class ProductoDetalle(APIView):
    def get(self, request, codigo):
        prod = get_object_or_404(Producto, Q(codigo=codigo)|Q(codigo_barra=codigo))
        data = ProductoSerializer(prod).data
        return Response(data)
        

class NotificacionList(APIView):
    def get(self, request, codigo):
        notif = Notificacion.objects.filter(user_destino=codigo, estado=True)
        data = NotificacionSerializer(notif, many=True).data
        return Response(data)



