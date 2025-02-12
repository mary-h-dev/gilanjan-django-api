from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BlogListView, BlogCategoryModelViewSet, BlogVisitCountView,
    BlogCommentsCreateView, BlogCommentsListView,
    BlogCreateView, BlogUpdateView, BlogLikeCountView, BlogDetailView,
    BlogCommentsUpdateView, BlogCommentsDetailView
)

router = DefaultRouter()
router.register('blog-category', BlogCategoryModelViewSet, basename="blog_cat")

urlpatterns = [
    path('', include(router.urls)),
    path('bg/create', BlogCreateView.as_view(), name='blog-create'),
    path('bg/list', BlogListView.as_view(), name='blog-list'),
    path('bg/update/<uuid:id>/', BlogUpdateView.as_view(), name='blog-update'),
    path('bg/detail/<uuid:id>/', BlogDetailView.as_view(), name='blog-detail'),
    # Comments
    path('bg-comments/list', BlogCommentsListView.as_view(), name='blog-comments-list'),
    path('bg-comments/create/', BlogCommentsCreateView.as_view(), name='blog-comments-create'),
    path('bg-comments/update/<int:id>/', BlogCommentsUpdateView.as_view(), name='blog-comments-update'),
    path('bg-comments/detail/<int:id>/', BlogCommentsDetailView.as_view(), name='blog-comments-detail'),
    # Like & Visit
    path('blogvisit/<uuid:blog_id>/', BlogVisitCountView.as_view(), name='blog_visit'),
    path('bloglike/<uuid:blog_id>/', BlogLikeCountView.as_view(), name='blog_like'),
]
