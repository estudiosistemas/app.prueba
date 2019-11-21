from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse

from django.views import generic

from .models import Notificacion
from .forms import NotificacionForm


class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):
    raise_exception=False
    redirect_field_name='redirect_to'
    login_url = 'bases:login'

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name='base/home.html'
    login_url='bases:login'

class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    template_name='base/sin_privilegios.html'
    login_url = 'bases:login'


class VistaBaseCreate(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    context_object_name='obj'
    success_message = 'Registro Agregado satisfactoriamente'   

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class VistaBaseEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    context_object_name='obj'
    success_message = 'Registro Actualizado Satisfactoriamente'   

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


# Vistas para las notificaciones
class NotificacionView(SinPrivilegios, generic.ListView ):
    permission_required = 'bases.view_notificacion'
    model = Notificacion
    template_name = 'base/notificacion_list.html'
    context_object_name = 'obj'

    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by a variable captured from url, for example
        return qs.filter(user_destino = self.request.user.id)


class NotificacionNew(VistaBaseCreate):
    permission_required = 'bases.add_notificacion'
    model = Notificacion
    template_name='base/notificacion_form.html'
    form_class=NotificacionForm
    success_url=reverse_lazy('bases:notificacion_list')


@login_required(login_url='/login/')
@permission_required('bases.change_notificacion', login_url='bases:sin_privilegios')
def notificacion_leer(request, id):
    notif = Notificacion.objects.filter(pk=id).first()
    if request.method=='POST':
        if notif:
            notif.estado= not notif.estado 
            notif.save()
            return HttpResponse('OK')
        return HttpResponse('FAIL')
    return HttpResponse('FAIL')


# class NotificacionRead(SinPrivilegios, generic.ListView ):
#     permission_required = 'bases.view_notificacion'
#     model = Notificacion
#     template_name = 'base/notificacion_read.html'
#     context_object_name = 'obj'

#     def get_queryset(self):
#         return  Notificacion.objects.get(id=3)

@login_required(login_url='/login/')
@permission_required('bases.change_notificacion', login_url='bases:sin_privilegios')
def notificacion_read(request, id):
    template_name='base/notificacion_read.html'
    contexto={}
    notif = Notificacion.objects.filter(pk=id).first()

    if not notif:
        return HttpResponse('Notificacion no existe ' + str(id) )

    if request.method=='GET':
        contexto={'obj': notif}

    return render(request,template_name, contexto)


# class UserProfile(VistaBaseEdit):
#     permission_required = ''
#     model = UserProfileForm
#     template_name='base/profile_form.html'
#     form_class=UserProfile
#     success_url=reverse_lazy('bases:home')