from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
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


def settings(request):
   profile_form = ProfileUpdateForm(instance=request.user.profile)
   user_form = UserUpdateForm(instance=request.user)

   if request.method == 'POST':
      profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
      user_form = UserUpdateForm(request.POST, instance=request.user)
      
      if user_form.is_valid() and profile_form.is_valid():
         profile_form.save()
         user_form.save()
         messages.success(request, f'Ваш аккаунт был успешно обнавлен!')
         return redirect('accounts:profile')

   return render(request, 'accounts/settings.html', context={
      'profile_form': profile_form,
      'user_form': user_form,
   })


def test(request):
   return render(request, 'accounts/test.html', context={
      
   })


def choose(request):
   variant = request.GET.get('inputValue')
   
   if variant == 'Дизайн' or variant == 'Разработка':
      result = JsonResponse({"question": "Аналитика документаций или аналитика интерфейса","first_new_variant":"Документация", "second_new_variant":"Интерфейс"})
   elif variant == 'Документация' or variant == 'Интерфейс':
      result = JsonResponse({"question": "Софт разработка или мобильная","first_new_variant":"Софт", "second_new_variant":"Мобильная"})
   elif variant == 'Софт' or variant == 'Мобильная':
      result = JsonResponse({"question": "Разработка части клиента или сервера","first_new_variant":"Клиент", "second_new_variant":"Сервер"})

   return result