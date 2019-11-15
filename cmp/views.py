from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse

import json, datetime
from django.db.models import Sum
from django.utils import timezone


from .models import Proveedor, ComprasEnc, ComprasDet
from .forms import ProveedorForm, ComprasEncForm
from bases.views import SinPrivilegios
from inv.models import Producto


class ProveedorView(SinPrivilegios, generic.ListView ):
    permission_required = 'cmp.view_proveedor'
    model = Proveedor
    template_name = 'cmp/proveedo_list.html'
    context_object_name = 'obj'


class ProveedorNew(SuccessMessageMixin,SinPrivilegios, generic.CreateView):
    permission_required = 'cmp.add_proveedor'
    model = Proveedor
    template_name='cmp/proveedor_form.html'
    context_object_name='obj'
    form_class=ProveedorForm
    success_url=reverse_lazy('cmp:proveedor_list')

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProveedorEdit(SuccessMessageMixin,SinPrivilegios, generic.UpdateView):
    permission_required = 'cmp.change_proveedor'
    model = Proveedor
    template_name='cmp/proveedor_form.html'
    context_object_name='obj'
    form_class=ProveedorForm
    success_url=reverse_lazy('cmp:proveedor_list')

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url='/login/')
@permission_required('inv.change_proveedor', login_url='bases:sin_privilegios')
def proveedor_inactivar(request, id):
    template_name='cmp/proveedor_inactivar.html'
    contexto={}
    prv = Proveedor.objects.filter(pk=id).first()

    if not prv:
        return HttpResponse('Proveedor no existe ' + str(id) )

    if request.method=='GET':
        contexto={'obj': prv}

    if request.method=='POST':
        prv.estado=False
        prv.save()
        contexto={'obj':'OK'}
        return HttpResponse('Proveedor Inactivado')

    return render(request,template_name, contexto)


 
class ComprasView(SinPrivilegios, generic.ListView ):
    permission_required = 'cmp.view_comprasenc'
    model = ComprasEnc
    template_name = 'cmp/compras_list.html'
    context_object_name = 'obj'


@login_required(login_url='/login/')
@permission_required('cmp.view_comprasenc', login_url='bases:sin_privilegios') 
def compras(request,compra_id=None):
    template_name='cmp/compras.html'
    prod=Producto.objects.filter(estado=True)
    form_compras={}
    contexto={}

    if request.method=='GET':
        form_compras=ComprasEncForm()
        enc = ComprasEnc.objects.filter(pk=compra_id).first()

        if enc:
            det = ComprasDet.objects.filter(compra=enc)
            fecha_compra = datetime.date.isoformat(enc.fecha_compra)
            fecha_factura = datetime.date.isoformat(enc.fecha_factura)
            e = {
                'fecha_compra': fecha_compra,
                'proveedor': enc.proveedor,
                'observacion': enc.observacion,
                'no_factura': enc.no_factura,
                'fecha_factura': fecha_factura,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total': enc.total
            }
            form_compras = ComprasEncForm(e)
        else:
            det = None
        
        contexto={
            'productos': prod,
            'encabezado': enc,
            'detalle': det,
            'form_enc': form_compras
        }

    if request.method=='POST':
        fecha_compra = request.POST.get('fecha_compra')
        observacion = request.POST.get('observacion')
        no_factura = request.POST.get('no_factura')
        fecha_factura = request.POST.get('fecha_factura')
        proveedor = request.POST.get('proveedor')
        subtotal = 0
        descuento = 0
        total = 0

        if not compra_id:
            prov=Proveedor.objects.get(pk=proveedor)
            enc = ComprasEnc(
                fecha_compra=fecha_compra,
                observacion=observacion,
                no_factura=no_factura,
                fecha_factura=fecha_factura,
                proveedor=prov,
                uc = request.user
            )
            if enc:
                enc.save()
                compra_id=enc.id
        else:
            enc = ComprasEnc.objects.filter(pk=compra_id).first()
            if enc:
                fecha_compra=fecha_compra
                observacion=observacion
                no_factura=no_factura
                fecha_factura=fecha_factura
                uc = request.user
                enc.save()
        
        if not compra_id:
            return redirect('comp:compra_list')

        producto = request.POST.get('id_id_producto')
        cantidad = request.POST.get('id_cantidad_detalle')
        precio = request.POST.get('id_precio_detalle')
        sub_total_detale = request.POST.get('id_sub_total_detalle')
        descuento_detalle = request.POST.get('id_descuento_detalle')
        total_detalle = request.POST.get('id_total_detalle')

        prod = Producto.objects.get(pk=producto)

        det = ComprasDet(
            compra=enc,
            producto=prod,
            cantidad=cantidad,
            precio_prv=precio,
            descuento=descuento_detalle,
            costo=0,
            uc = request.user
        )

        if det:
            det.save()
            # sub_total = ComprasDet.objects.filter(compra=compra_id).aggregate(sum('sub_total'))
            # descuento = ComprasDet.objects.filter(compra=compra_id).aggregate(sum('descuento'))
            # enc.sub_total = sub_total['sub_total__sum']
            # enc.descuento = descuento['descuento__sum']
            sub_total = ComprasDet.objects \
                        .filter(compra=compra_id) \
                        .aggregate(sub_total=Sum('sub_total')) \
                        .get('sub_total', 0.00)
            enc.sub_total=sub_total
            descuento = ComprasDet.objects \
                        .filter(compra=compra_id) \
                        .aggregate(descuento=Sum('descuento')) \
                        .get('descuento', 0.00)
            enc.descuento=descuento
            enc.save()

        return redirect('cmp:compra_edit', compra_id=compra_id)

    return render(request, template_name, contexto)


class CompraDetDelete(SinPrivilegios, generic.DeleteView):
    permission_required = 'cmp.delete_comprasdet'
    model = ComprasDet
    template_name='cmp/compras_det_del.html'
    context_object_name = 'obj'

    def get_success_url(self):
        compra_id=self.kwargs['compra_id']
        return reverse_lazy('cmp:compra_edit', kwargs={'compra_id': compra_id})
