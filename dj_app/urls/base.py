from django.urls import path

from dj_app.views import auth, start

urlpatterns = [
    path("", auth.LandingPage.as_view(), name="home"),
    path("start/", start.Start.as_view(), name="start"),
]
