from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from bases.models import Profile


@login_required(login_url='/login/')
def profileUser(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Su cuenta ha sido actualizada!')
            return redirect('usr:perfil_usuario')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'usr/perfil.html', context)


@login_required(login_url='/login/')
def registerUser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            cod = User.objects.last()
            profile = Profile.objects.create(user=cod, image='default.jpg')
            messages.success(request, f'Cuenta creada para {username}!')
            return redirect('bases:home')
    else:
        form = UserRegisterForm()
    return render(request, 'usr/registrar.html', {'form':form})
