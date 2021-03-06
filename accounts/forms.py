from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ValidationError

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

      

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('email','first_name','last_name')

   #  def clean_username(self):
   #      new_username = self.cleaned_data['username']

   #      if User.objects.filter(username=new_username).exists():
   #          raise ValidationError('Имя пользователя {} уже существует.'.format(new_username))
   #      return new_username


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'position',
            'information',
            'job',
            'date_birth', 
            'phone', 
            'country',
            'city',
            'img'
        )
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['position'].label = "Должность"
        self.fields['information'].label = "О себе"
        self.fields['job'].label = "Место работы"
        self.fields['date_birth'].label = "Дата рождения"
        self.fields['phone'].label = "Номер телефона"
        self.fields['country'].label = "Страна"
        self.fields['city'].label = "Город"
        self.fields['img'].label = "Изображение профиля"
        
        
    
    