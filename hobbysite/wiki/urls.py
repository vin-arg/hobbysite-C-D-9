from django.urls import path
from .views import article_list_view, article_detail_view

app_name = "wiki"

urlpatterns = [
    path("articles/", article_list_view, name="articles"),
    path("article/<int:pk>/", article_detail_view, name="article_detail"),
]