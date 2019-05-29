# from .forms import UserUpdateForm, ProfileUpdateForm
# from django.shortcuts import redirect
# from django.contrib import messages

# def profile_update_form(request):
#    profile_form = ProfileUpdateForm()
#    user_form = UserUpdateForm()

#    if request.method == 'POST':
#       profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#       user_form = UserUpdateForm(request.POST, instance=request.user)
      
#       if user_form.is_valid() and profile_form.is_valid():
#          profile_form.save()
#          user_form.save()
#          messages.success(request, f'Ваш аккаунт был успешно обнавлен!')
#          return redirect('acccounts:profile')
#       else:
#          return {
#             'profile_form': profile_form,
#             'user_form': user_form,
#          }
#    return {
#       'profile_form': profile_form,
#       'user_form': user_form,
#    }