from django.urls import path
from . import views

app_name = "commissions"

urlpatterns = [
    path('list/', views.commissions_list, name = 'commissions_list'),
    path('detail/<int:pk>', views.commissions_detail, name = 'commissions_detail'),
    path('add/', views.commissions_list, name = 'commissions_add'),
    path('<int:pk>/edit', views.commissions_detail, name = 'commissions_edit'),
]