from django.conf.urls import url, include
from users.views import dashboard
from output.views import result

urlpatterns = [
    url("", dashboard, name="dashboard"),
    url("output", include('output.urls')),
    url("output", result, name="output"),
]