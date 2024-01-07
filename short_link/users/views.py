from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserOurRegistration, UserUpdateForm


def register(request):
    if request.method == "POST":
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')
    else:
        form = UserOurRegistration()
    return render(request, 'users/registraion.html', {'form': form, 'title': 'Регистрация пользователя'})


@login_required
def profile(request):
    if request.method == "POST":
        update_user = UserUpdateForm(request.POST, instance=request.user)

        if update_user.is_valid():
            update_user.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
    else:
        update_user = UserUpdateForm(instance=request.user)

    data = {
        'update_user': update_user
    }

    return render(request, 'users/profile.html', data)
