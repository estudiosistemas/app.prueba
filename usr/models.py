from django.db import models
from django.contrib.auth.models import User
from PIL import Image




# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #agencias = models.ManyToManyField('bases_models.Agencia', through='bases_models.User_Agencia')

    def __str__(self):
        return f'{self.user.username}'

    def save(self,force_insert=False, force_update=False, using=None):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width  > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)