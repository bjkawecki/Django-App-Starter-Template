from django.urls import path

from dj_app.views import errors

urlpatterns = [
    path("404/", errors.Error404.as_view(), name="error_404"),
]
