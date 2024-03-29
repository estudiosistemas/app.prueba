# Generated by Django 2.2.6 on 2019-12-18 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=150)),
                ('domicilio', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=150)),
                ('logo', models.ImageField(upload_to='logo_pics')),
            ],
            options={
                'verbose_name_plural': 'Agencias',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Codigo_Postal',
            fields=[
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('localidad', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Códigos Postales',
            },
        ),
        migrations.CreateModel(
            name='Condicion_IVA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=50)),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Iva',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Provincias',
                'ordering': ('codigo',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('agencias', models.ManyToManyField(to='bases.Agencia')),
            ],
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('asunto', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=200)),
                ('leida', models.BooleanField(default=False)),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Notificaciones',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=150)),
                ('domicilio', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=150)),
                ('cuit', models.CharField(max_length=150)),
                ('iibb', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='logo_pics')),
                ('codigo_postal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bases.Codigo_Postal')),
                ('iva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bases.Condicion_IVA')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.AddField(
            model_name='codigo_postal',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bases.Provincia'),
        ),
        migrations.AddField(
            model_name='codigo_postal',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='codigo_postal',
            name='um',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agencia',
            name='codigo_postal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codpostal', to='bases.Codigo_Postal'),
        ),
        migrations.AddField(
            model_name='agencia',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bases.Empresa'),
        ),
        migrations.AddField(
            model_name='agencia',
            name='localidades',
            field=models.ManyToManyField(to='bases.Codigo_Postal'),
        ),
        migrations.AddField(
            model_name='agencia',
            name='uc',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agencia',
            name='um',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
