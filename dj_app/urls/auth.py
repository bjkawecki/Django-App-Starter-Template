from allauth.account.views import PasswordResetView
from django.urls import path

from dj_app.views.auth import LoginPage, SignupPage, logout_user

urlpatterns = [
    path("logout/", logout_user, name="logout"),
    path("signup/", SignupPage.as_view(), name="signup"),
    path("signin/", LoginPage.as_view(), name="signin"),
    path(
        "account-reset-password/",
        PasswordResetView.as_view(),
        name="account_reset_password",
    ),
]
