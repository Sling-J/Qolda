from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'
urlpatterns = [
    path('sign-in/', LoginView.as_view(template_name='accounts/signin.html'), name='signin'),
    path('sign-up/', views.sign_up, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('settings/', views.settings, name='settings_url'),
    path('test/', views.test, name='test_url'),
    path('choose/', views.choose, name='choose_url')
]