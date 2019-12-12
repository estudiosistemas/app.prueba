from django.urls import path

from .views import ProveedorView, ProveedorEdit, ProveedorNew, proveedor_inactivar, \
    ComprasView, compras, CompraDetDelete, Home, proveedor_activar

from .reportes import reporte_compras, imprimir_compra

urlpatterns = [
    path('',Home.as_view(), name='compras_home'),
    path('proveedores/',ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedores/inactivar/<int:id>', proveedor_inactivar, name='proveedor_inactivar'),
    path('proveedores/estado/<int:id>', proveedor_activar, name='proveedor_activar'),

    path('compras/',ComprasView.as_view(), name='compra_list'),
    path('compras/new',compras, name='compra_new'),
    path('compras/edit/<int:compra_id>',compras, name='compra_edit'),
    path('compras/<int:compra_id>/delete/<int:pk>',CompraDetDelete.as_view(), name='compra_del'),

    path('compras/listado', reporte_compras, name='compras_print_all'),
    path('compras/<int:compra_id>/imprimir', imprimir_compra, name='compras_print_one'),
]