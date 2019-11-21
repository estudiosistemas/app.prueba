from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey
from django.contrib.auth.models import User
from usr.models import Profile

class MyModel(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = UserForeignKey(auto_user_add=True, related_name="+")
    um = UserForeignKey(auto_user=True, related_name="+")

    class Meta:
        abstract=True


class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract=True


# MODELO NOTIFICACIONES
class Notificacion(MyModel):
    asunto = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=200)
    user_destino = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.mensaje)

    def save(self):
        self.asunto=self.asunto.upper()
        self.mensaje=self.mensaje.upper()
        super(Notificacion, self).save()

    class Meta:
        verbose_name_plural = "Notificaciones"


