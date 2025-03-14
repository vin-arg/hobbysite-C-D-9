from django.urls import path
from .views import ArticleListView, ArticleDetailView

app_name = "wiki"

urlpatterns = [
    path("articles/", ArticleListView.as_view(), name="articles"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
]