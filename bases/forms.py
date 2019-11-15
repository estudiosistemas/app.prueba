from django import forms

from .models import Notificacion

class NotificacionForm(forms.ModelForm):
    class Meta:
        model = Notificacion
        fields=['user_destino', 'asunto','mensaje']
        exclude = ['um', 'fm', 'uc', 'fc']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })