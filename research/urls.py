from django.urls import URLPattern
from django.urls import path
from research import views

app_name = "research"

urlpatterns = [path("research/", views.Research, name="research")]
