from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey
from usr.models import Profile

#Clase Modelo para todos los modelos
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
    leida = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.mensaje)

    def save(self):
        self.asunto=self.asunto.upper()
        self.mensaje=self.mensaje.upper()
        super(Notificacion, self).save()

    class Meta:
        verbose_name_plural = "Notificaciones"


#MODELO PROVINCIAS
class Provincia(MyModel):
    codigo = models.CharField(max_length=1, primary_key=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.codigo=self.codigo.upper()
        self.nombre=self.nombre.upper()
        super(Provincia, self).save()

    class Meta:
        ordering = ('codigo',)
        verbose_name_plural = "Provincias"


#MODELO COD_POSTALES
class Codigo_Postal(MyModel):
    codigo = models.CharField(max_length=4)
    localidad = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.localidad, self.provincia)

    def save(self):
        self.localidad=self.localidad.upper()
        super(Codigo_Postal, self).save()

    class Meta:
        verbose_name_plural = "Códigos Postales"


#MODELO Condiciones de IVA
class Condicion_IVA(MyModel):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre=self.nombre.upper()
        super(Condicion_IVA, self).save()

    class Meta:
        verbose_name_plural = "Iva"


#MODELO EMPRESA
class Empresa(MyModel):
    nombre = models.CharField(max_length=150)
    domicilio = models.CharField(max_length=150)
    codigo_postal = models.ForeignKey(Codigo_Postal, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=150)
    iva = models.ForeignKey(Condicion_IVA, on_delete=models.CASCADE)
    cuit = models.CharField(max_length=150)
    inicio_actividades = models.DateField
    iibb = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo_pics')

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre=self.nombre.upper()
        self.domicilio=self.domicilio.upper()
        super(Empresa, self).save()

    class Meta:
        verbose_name_plural = "Empresas"


#MODELO Agencias
class Agencia(MyModel):
    nombre = models.CharField(max_length=150)
    domicilio = models.CharField(max_length=150)
    codigo_postal = models.ForeignKey(
        Codigo_Postal, 
        on_delete=models.CASCADE,
        related_name='codpostal'
    )
    telefono = models.CharField(max_length=150)
    porcentaje = models.FloatField
    porcentaje_Bs_As = models.FloatField
    logo = models.ImageField(upload_to='logo_pics')
    localidades = models.ManyToManyField(Codigo_Postal, through='CP_Agencia')
    usuarios = models.ManyToManyField(Profile, through='User_Agencia')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre=self.nombre.upper()
        super(Agencia, self).save()

    class Meta:
        verbose_name_plural = "Agencias"


# #MODELO Postales por Agencia
class CP_Agencia(models.Model):
    agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE)
    codigo_postal = models.ForeignKey(Codigo_Postal, on_delete=models.CASCADE)


#MODELO Usuarios por Agencia
class User_Agencia(models.Model):
    agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Profile, on_delete=models.CASCADE)





