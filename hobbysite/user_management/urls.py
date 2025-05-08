from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home_page, name="home_page")
    # path("profile", profile, name="profile"),
]