from django.shortcuts import render, redirect
from allauth.account import views
from django.views.generic import View
from django.contrib.auth import views as auth_views

# Create your views here.
class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'

class LogoutView(auth_views.LogoutView):
    template_name = 'accounts/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')

class SignupView(views.SignupView):
    template_name = 'accounts/signup.html'

