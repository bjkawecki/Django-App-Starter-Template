from allauth.account.forms import SignupForm
from django import forms

from starter_app.models.user import User


class RegisterUserForm(SignupForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    field_order = ["email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["placeholder"] = "beispiel@mail.de"
        self.fields["password1"].widget.attrs["placeholder"] = "Mindestens 8 Zeichen"
        self.fields["password2"].widget.attrs["placeholder"] = "Erneut eingeben"

        for fieldname in ["password1", "password2"]:
            self.fields[fieldname].help_text = None

    def signup(self, request, user):
        pass

    email = forms.EmailField(
        max_length=30, label="E-Mail", required=True, show_hidden_initial="Email"
    )
    password1 = forms.CharField(
        max_length=30, label="Passwort", required=True, widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        max_length=30,
        label="Passwort (wiederholen)",
        required=True,
        widget=forms.PasswordInput,
    )
