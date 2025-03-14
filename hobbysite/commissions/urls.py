from django.urls import path
from . import views

app_name = "commissions"

urlpatterns = [
    path('list/', views.commissions_list, name = 'commissions_list'),
    path('detail/<int:pk>', views.commissions_detail, name = 'commissions_detail'),
]