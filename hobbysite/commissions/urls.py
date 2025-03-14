from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path("commissions/list", views.recipeList, name = "commissions_list"),
    path("item/<int:num>", views.recipe1, name = "commissions_detail"),
]

app_name = "commissions"