from django.conf.urls import url
from output.views import result

urlpatterns = [
    url("", result, name="output")
]