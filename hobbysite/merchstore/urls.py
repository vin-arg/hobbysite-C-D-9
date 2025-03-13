from django.urls import path
from .views import *

urlpatterns = [
    path("items/", itemList, name="itemList"),
    path("item/<int:num>", itemEntry, name="itemEntry"),
]