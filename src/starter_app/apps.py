from django.apps import AppConfig


class StarterConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "starter_app"

    def ready(self):
        import starter_app.signals  # noqa : F821
