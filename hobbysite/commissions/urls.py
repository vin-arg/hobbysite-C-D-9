from django.urls import path
from . import views

urlpatterns = [
    path("commissions/list", views.commissions_list, name = "commissions_list"),
    path("item/<int:pk>", views.commissions_detail, name = "commissions_detail"),
]

app_name = "commissions"