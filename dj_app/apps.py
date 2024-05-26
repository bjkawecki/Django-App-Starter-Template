from django.apps import AppConfig


class TrainerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dj_app"

    def ready(self):
        import dj_app.signals  # noqa : F821
