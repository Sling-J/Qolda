from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserOurRegistration, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import redirect
from django.contrib import messages


def sign_up(request):
    if request.method == 'POST':
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} создан, введите имя пользователя и пароль для авторизации')
            return redirect('accounts:signin')
    form = UserOurRegistration()
    return render(request, 'accounts/signup.html', {'form':form})

@login_required(login_url='accounts:signin')
def profile(request):
    user = request.user
    saved_recommendations = request.user.saver_set.all()
    my_recommendations = request.user.recommendation_set.all()
    return render(request, 'accounts/profile.html', {
        'user': user,
        'saved_recommendations': saved_recommendations,
        'my_recommendations': my_recommendations,
    })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('static_pages:index'))