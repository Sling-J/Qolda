from .forms import UserUpdateForm, ProfileUpdateForm
from django.shortcuts import redirect
from django.contrib import messages

def profile_update_form(request):
   user_form = UserUpdateForm(instance=request.user)
   profile_form = ProfileUpdateForm(instance=request.user.profile)

   if request.method == 'POST':
      user_form = UserUpdateForm(request.POST, instance=request.user)
      profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

      if user_form.is_valid() and profile_form.is_valid():
         user_form.save()
         profile_form.save()
         messages.success(request, f'Ваш аккаунт был успешно обнавлен!')
         return redirect('acccounts:profile')
   return {
      'user_form': user_form,
      'profile_form': profile_form,
   }



   
