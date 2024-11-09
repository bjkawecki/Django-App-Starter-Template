AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# --------------------------------------------------------------
# ALL_AUTH
# --------------------------------------------------------------

LOGIN_URL = "signin"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 600  # 10 minutes
LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_CHANGE_EMAIL = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
ACCOUNT_FORMS = {
    "signup": "starter_app.forms.register.RegisterUserForm",
    # "change_password": "starter_app.forms.password.ChangeUserPasswordForm",
    # "login": "starter_app.forms.login.LoginUserForm",
}
FILTERS_DISABLE_HELP_TEXT = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""
AUTH_USER_MODEL = "starter_app.User"
