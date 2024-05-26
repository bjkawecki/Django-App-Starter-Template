from allauth.account.views import LoginView, SignupView
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView

from config.settings.common import VERSION


def logout_user(request):
    logout(request)
    messages.success(request, ("Abgemeldet. До встречи!"))
    return redirect("home")


class LandingPage(TemplateView):
    template_name = "landing.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse("start"))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["version"] = VERSION
        return context


class LoginPage(LoginView):
    template_name = "landing.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse("start"))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["version"] = VERSION
        return context


class SignupPage(SignupView):
    template_name = "signup.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse("start"))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["version"] = VERSION
        return context
