# awesome_website/urls.py

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url("", include("users.urls")),
    url("admin", admin.site.urls),
    url("output", include('output.urls')),
]