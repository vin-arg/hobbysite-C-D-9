from django.urls import path
from . import views

app_name = "commissions"

urlpatterns = [
    path('list/', views.commission_list, name = 'commissions_list'),
    path('detail/<int:pk>', views.commission_detail, name = 'commissions_detail'),
    path('add/', views.commission_create, name = 'commissions_add'),
    path('<int:pk>/edit', views.commission_detail, name = 'commissions_edit'),
]