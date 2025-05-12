from django.urls import path
from .views import home_page

urlpatterns = [
    path('home/', home_page, name="home_page")
    # path("profile", profile, name="profile"),
]


print("user_management urls loaded")