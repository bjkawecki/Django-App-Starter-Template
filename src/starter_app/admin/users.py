from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from starter_app.forms.user import UserCreationForm
from starter_app.models.user import User


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    list_display = ("email", "first_name", "last_name", "is_staff", "is_active")
    readonly_fields = ["id"]
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    fieldsets = (
        (
            "Allgemein",
            {
                "fields": (
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "id",
                    "subscription",
                    "customer",
                )
            },
        ),
        (
            "Einstellungen",
            {
                "fields": (
                    "daily_proverb",
                    "daily_proverb_updated",
                    "show_welcome_modal",
                    "is_deck_name_russian",
                    "show_examples",
                )
            },
        ),
        (
            "Erlaubnisse",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Datumsfelder", {"fields": ("last_login", "date_joined")}),
    )

    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
