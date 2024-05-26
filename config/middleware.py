from django.shortcuts import redirect

from config.settings.common import ADMIN_URL


class CheckUser(object):

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        if (
            not request.user.is_authenticated
            and request.path != "/"
            and not request.path.startswith("/signin")
            and not request.path.startswith("/signup")
            and not request.path.startswith("/accounts")
            and not request.path.startswith("/account-reset-password")
            and not request.path.startswith("/404")
            and not request.path.startswith(f"/{ADMIN_URL}")
        ):
            return redirect("error_404")

        response = self.get_response(request)
        return response
