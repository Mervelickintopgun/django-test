from django.urls import path
from accounts import views

from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('login1/', views.LoginView.as_view(), name='account_login'),
    # path('logout1/', views.LogoutView.as_view(), name='account_logout'),
    path('signup1/', views.SignupView.as_view(), name='account_signup'),

    path('login/', auth_views.LoginView.as_view(), name='login'), # 追加
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # 追加
    path('oauth/', include('social_django.urls', namespace='social')), # 追加
    # path('accounts/profile/', views.index, name='index'), # 追加

]

