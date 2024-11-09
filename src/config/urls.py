from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config.settings.common import ADMIN_URL, DEBUG

urlpatterns = [
    path(f"{ADMIN_URL}/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("starter_app.urls.auth")),
    path("", include("starter_app.urls.base")),
    path("", include("starter_app.urls.errors")),
]
if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)


admin.site.site_header = "YOUR SITE HEADER NAME"
admin.site.index_title = "INDEX_TITLE"
