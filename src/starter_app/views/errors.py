from django.views.generic import TemplateView

from config.settings.common import VERSION


class Error404(TemplateView):
    template_name = "404.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["version"] = VERSION
        return context
