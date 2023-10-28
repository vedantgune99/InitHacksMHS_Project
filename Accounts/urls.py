from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [

    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('signin/', views.signin_user, name='signin_user'),


     # Password Reset Points...
    path('reset_password/',  auth_views.PasswordResetView.as_view(template_name='reset_password.html'),
         name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_email_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset_confirm.html"),
         name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_finished.html"),
         name="password_reset_complete"),

]