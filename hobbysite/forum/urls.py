from django.urls import path
from . import views

app_name = "forum"

urlpatterns = [
    path("threads/", views.thread_list, name="thread_list"),
    path("thread/<int:pk>/", views.thread_detail, name="thread_detail"),
    path("category/<int:category_id>/", views.posts_by_category, name="posts_by_category"),  
]
