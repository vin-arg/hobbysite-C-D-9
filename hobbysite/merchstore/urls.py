from django.urls import path
from .views import *

urlpatterns = [
    path("items/", item_list, name="item_list"),
    path("item/<int:num>", item_entry, name="item_entry"),
    path("item/add", item_add, name="item_add"),
    path("item/edit/<int:num>", item_edit, name="item_edit"),
    path("item/cart", item_cart, name="item_cart"),
    path("item/transactions", item_transactions, name="item_transactions"),
]