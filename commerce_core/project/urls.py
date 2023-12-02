from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import commerce_core.auctions.urls
import commerce_core.authentication.urls

API_PREFIX = "api/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(API_PREFIX, include(commerce_core.auctions.urls)),
    path(API_PREFIX, include(commerce_core.authentication.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
