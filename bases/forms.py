from django import forms
from django.core.files.images import get_image_dimensions

from .models import Notificacion, Provincia

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
    class Meta:
        model = Notificacion
        fields=['user_destino', 'asunto','mensaje']
        exclude = ['um', 'fm', 'uc', 'fc']

    

class ProvinciaForm(MyModelForm):
    class Meta:
        model=Provincia
        fields = ['codigo','nombre', 'estado']

        exclude = ['um', 'fm', 'uc', 'fc']
        
