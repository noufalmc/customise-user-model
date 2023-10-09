from django.urls import path
from . import views

from dj_rest_auth.registration.views import RegisterView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView

app_name = "accounts"

urlpatterns = [
    # FOR DJ-REST-AUTH PACKAGE URLS
    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

]
