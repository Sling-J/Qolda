from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class SigninForm(forms.Form):
#     email = forms.CharField(
#     label = "",
#     widget = forms.TextInput(attrs={
#         'class':'email',
#         'placeHolder':'Email'
#     }))
#     password = forms.CharField(
#     label = "",
#     widget = forms.PasswordInput(attrs={
#         'class':'password',
#         'placeholder':'Введите пароль'
#     }))


# class SignupForm(forms.Form):
#     email = forms.CharField(
#         label = "",
#         widget = forms.TextInput(attrs={
#         'class':'input',
#         'placeHolder':'Email'
#     }))
#     username = forms.CharField(
#         label = "",
#         widget = forms.TextInput(attrs={
#         'class':'input',
#         'placeHolder':'Полное имя'
#     }))
#     password = forms.CharField(
#         label = "",
#         widget = forms.PasswordInput(attrs={
#         'class':'input',
#         'placeholder':'Пароль'
#     }))
#     password_repeat = forms.CharField(
#         label = "",
#         widget = forms.PasswordInput(attrs={
#         'class':'input',
#         'placeholder':'Введите пароль повторно'
#     }))


class UserOurRegistration(UserCreationForm):
   email = forms.EmailField(required=True)
   
   class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name','password1','password2')

        widgets = {
            'username': forms.TextInput(attrs={'class':'input', 'placeHolder':'Логин'}),
            'email': forms.TextInput(attrs={'class':'input', 'placeHolder':'Email'}),
            'first_name': forms.TextInput(attrs={'class':'input', 'placeHolder':'Имя'}),
            'last_name': forms.TextInput(attrs={'class':'input', 'placeHolder':'Фамилия'}),
            'password1': forms.PasswordInput(attrs={'class':'input', 'placeHolder':'Введите пароль'}),
            'password2': forms.PasswordInput(attrs={'class':'input', 'placeHolder':'Введите пароль повторно'})
        } 
    
    