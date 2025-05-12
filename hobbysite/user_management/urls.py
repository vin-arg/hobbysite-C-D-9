from django.urls import path
from .views import home_page, register

urlpatterns = [
    path('home/', home_page, name="home_page"),
    path('register/', register, name='register'),
    # path("profile", profile, name="profile"),
]
