from django.shortcuts import render, redirect
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from django.db.models import Q 
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


from rest_framework import generics, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import ProductoSerializer, NotificacionSerializer, ProvinciaSerializer, ClienteSerializer, Agencias_UserSerializer, AgenciaSerializer
from inv.models import Producto
from fac.models import Cliente
from bases.models import Notificacion, Provincia, Agencia
from bases.models import Profile


class Login(FormView):
    template_name = "base/login.html"
    form_class = AuthenticationForm

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            url = reverse_lazy('bases:select_agencia', kwargs={'id_usuario':request.user.id})
            return HttpResponseRedirect(url)
        else:
            return super(Login,self).dispatch(request,*args,*kwargs)

    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)

    def get_success_url(self, **kwargs):     
        return reverse_lazy('bases:select_agencia', kwargs={'id_usuario':self.request.user.id})  


class Logout(APIView):
    def get(self,request, format = None):
        try:
            request.user.auth_token.delete()
        except Exception as e:
            print(e)
        logout(request)
        return HttpResponseRedirect(reverse_lazy('bases:login'))


class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    

class ProductoDetalle(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, codigo):
        prod = get_object_or_404(Producto, Q(codigo=codigo)|Q(codigo_barra=codigo))
        data = ProductoSerializer(prod).data
        return Response(data)
        

class NotificacionList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, codigo):
        notif = Notificacion.objects.filter(user_destino=codigo, estado=True)
        data = NotificacionSerializer(notif, many=True).data
        return Response(data)


class NotificacionListWeb(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, codigo):
        notif = Notificacion.objects.filter(user_destino=codigo, estado=True)
        data = NotificacionSerializer(notif, many=True).data
        return Response(data)
        

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class ProvinciaList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer


class ClienteList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer    


    
class Agencias_User(APIView):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    
    def get(self, request, codigo):
        agen = get_object_or_404(Profile, user_id=codigo)
        data = Agencias_UserSerializer(agen).data
        return Response(data)