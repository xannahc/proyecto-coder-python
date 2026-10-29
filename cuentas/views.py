from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm, EditarPerfilForm

def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('blog:inicio')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, f"¡Bienvenido/a {usuario.username}!")
            return redirect('blog:inicio')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'

    return render(request, 'cuentas/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('blog:inicio')

def registro(request):
    if request.user.is_authenticated:
        return redirect('blog:inicio')

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, f"¡Cuenta creada con éxito! Bienvenido/a {usuario.username}.")
            return redirect('blog:inicio')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'cuentas/registro.html', {'form': form})

@login_required
def perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu perfil fue actualizado con éxito.")
            return redirect('cuentas:perfil')
    else:
        form = EditarPerfilForm(instance=request.user)

    posts_usuario = request.user.posts.all()
    return render(request, 'cuentas/perfil.html', {
        'form': form,
        'posts': posts_usuario
    })
