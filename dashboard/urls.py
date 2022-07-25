from django.urls import path

from .views import *

urlpatterns = [
    path("main-dashboard", main_dashboard, name="main_dashboard"),
]