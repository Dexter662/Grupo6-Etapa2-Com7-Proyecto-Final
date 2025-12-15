from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import ProfileForm, UsuarioAdminEditForm

User = get_user_model()


@login_required
def user_list(request):
    if request.user.rol != 'admin':
        return redirect('inicio')

    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


@login_required
def user_detail(request, pk):
    user_obj = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', {'user_obj': user_obj})


@login_required
def user_admin_edit(request, pk):
    if request.user.rol != 'admin':
        return redirect('inicio')

    user_obj = get_object_or_404(User, pk=pk)
    profile = getattr(user_obj, 'profile', None)

    if request.method == 'POST':
        user_form = UsuarioAdminEditForm(request.POST, instance=user_obj)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('users:detail', user_obj.id)
    else:
        user_form = UsuarioAdminEditForm(instance=user_obj)
        profile_form = ProfileForm(instance=profile)

    return render(
        request,
        'users/user_admin_form.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
            'user_obj': user_obj,
        }
    )


@login_required
def profile_edit(request):
    profile = getattr(request.user, 'profile', None)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:detail', request.user.id)
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'users/profile_form.html', {'form': form})


@login_required
def user_delete(request, pk):
    if request.user.rol != 'admin':
        return redirect('inicio')

    user_obj = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        user_obj.delete()
        return redirect('users:list')

    return render(request, 'users/user_confirm_delete.html', {'user_obj': user_obj})
