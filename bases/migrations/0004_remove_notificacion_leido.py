# Generated by Django 2.2.6 on 2019-11-10 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0003_notificacion_leido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificacion',
            name='leido',
        ),
    ]
