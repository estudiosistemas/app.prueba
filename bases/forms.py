from django import forms
from django.forms import BaseModelFormSet
from django.core.files.images import get_image_dimensions

from .models import Notificacion, Provincia, Codigo_Postal, Agencia, Profile

class MyModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

    class Meta:
        abstract=True


class NotificacionForm(MyModelForm):
    mensaje = forms.CharField( widget=forms.Textarea(attrs={"rows":3}) )
    class Meta:
        model = Notificacion
        fields=['user_destino', 'asunto','mensaje']

    

class ProvinciaForm(MyModelForm):
    class Meta:
        model=Provincia
        fields = ['codigo','nombre', 'estado']

        exclude = ['um', 'fm', 'uc', 'fc']
        

class CodigoPostalForm(MyModelForm):
    class Meta:
        model=Codigo_Postal
        fields = ['codigo','localidad', 'provincia']


class UserAgenciaForm(BaseModelFormSet):
    class Meta:
        model=Agencia
        fields = ['id','nombre']
        widgets = {'nombre': forms.Select() }