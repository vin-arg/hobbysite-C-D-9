from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home, name = "home"),
    path("recipes/list", views.recipeList, name = "recipeList"),
    path("recipe/1", views.recipe1, name = "recipe1"),
    path("recipe/2", views.recipe2, name = "recipe2")
]

app_name = "commissions"