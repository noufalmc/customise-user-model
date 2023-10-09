from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('api.v1.accounts.urls', namespace="accounts"))
]
