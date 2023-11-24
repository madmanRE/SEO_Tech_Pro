from django.urls import path
from .views import (
    BlogPostListView,
    BlogPostDetailView,
    BlogPostUpdateView,
    BlogCategoryView,
    search,
)

app_name = "blog"

urlpatterns = [
    path("article/update/<slug>/", BlogPostUpdateView.as_view(), name="update_post"),
    path("article/<slug:slug>/", BlogPostDetailView.as_view(), name="article"),
    path("", BlogPostListView.as_view(), name="blog"),
    path("search/", search, name="search"),
    path("<slug:cat_slug>/", BlogCategoryView, name="category"),
]
