from django.urls import path
from . import views

urlpatterns = [
    path("commissions/list", views.commissions_content, name = "commissions_list"),
    path("item/<int:num>", views.commissions_comments, name = "commissions_detail"),
]

app_name = "commissions"