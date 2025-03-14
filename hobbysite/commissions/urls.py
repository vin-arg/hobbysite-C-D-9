from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path("commissions/list", views.commissions_list, name = "commissions_list"),
    path("item/<int:num>", views.commissions_detail, name = "commissions_detail"),
]

app_name = "commissions"