from django import forms
from django.contrib.auth.forms import UserCreationForm

from starter_app.models.user import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class DeleteUserForm(forms.Form):
    confirm = forms.CharField(label="Bestätigen", max_length=7)

    def clean_confirm(self):
        confirm = self.cleaned_data.get("confirm")
        if confirm != "DELETE":
            raise forms.ValidationError("Falsche Eingabe.")
