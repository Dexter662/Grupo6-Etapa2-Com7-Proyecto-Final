from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from .forms import UserProfileForm

User = get_user_model()

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', {'user_obj': user})

@login_required
def profile_edit(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:detail', request.user.id)
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'users/profile_form.html', {'form': form})

@login_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.user.rol != 'admin':
        return redirect('users:list')

    if request.method == 'POST':
        user.delete()
        return redirect('users:list')

    return render(request, 'users/user_confirm_delete.html', {'user_obj': user})

