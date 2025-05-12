from django.urls import path
from .views import *

urlpatterns = [
    path("items/", item_list, name="item_list"),
    path("item/<int:num>", item_entry, name="item_entry"),
    path("item/add", item_add, name="item_add"),
    path("item/<int:num>/edit", item_edit, name="item_edit"),
]