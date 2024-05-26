from django.conf import settings


def project_context(request):
    context = {
        "stage": settings.STAGE,
        "support-email": "support@yourdomain.org",
        "app_name": "Django App",
    }

    return context
