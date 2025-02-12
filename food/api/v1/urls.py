from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FoodListView, FoodCategoryModelViewSet, FoodVisitCountView,
    FoodCommentCreateView, FoodCommentListView,
    FoodCreateView, FoodUpdateView, FoodLikeCountView, FoodDetailView,
    FoodCommentUpdateView, FoodCommentDetailView
)

router = DefaultRouter()
router.register('food-category', FoodCategoryModelViewSet, basename="food_cat")

urlpatterns = [
    path('', include(router.urls)),
    # Food URLs
    path('fd/create', FoodCreateView.as_view(), name='food-create'),
    path('fd/list', FoodListView.as_view(), name='food-list'),
    path('fd/update/<uuid:id>/', FoodUpdateView.as_view(), name='food-update'),
    path('fd/detail/<uuid:id>/', FoodDetailView.as_view(), name='food-detail'),
    # Comments URLs
    path('fd-comments/list', FoodCommentListView.as_view(), name='food-comments-list'),
    path('fd-comments/create', FoodCommentCreateView.as_view(), name='food-comments-create'),
    path('fd-comments/update/<int:id>/', FoodCommentUpdateView.as_view(), name='food-comments-update'),
    path('fd-comments/detail/<int:id>/', FoodCommentDetailView.as_view(), name='food-comments-detail'),
    # Like & Visit URLs
    path('foodvisit/<uuid:food_id>/', FoodVisitCountView.as_view(), name='food_visit'),
    path('foodlike/<uuid:food_id>/', FoodLikeCountView.as_view(), name='food_like'),
]
