from django.urls import path
from .views import (
    GalleryUploadView,
    GalleryListView,
    GalleryDetailView,
    PhotoListView,
    PhotoDetailView,
)

urlpatterns = [
    path('upload/', GalleryUploadView.as_view(), name='gallery-upload'),
    path('galleries/', GalleryListView.as_view(), name='gallery-list'),
    path('galleries/<int:pk>/', GalleryDetailView.as_view(), name='gallery-detail'),
    path('photos/', PhotoListView.as_view(), name='photo-list'),
    path('photos/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail'),
]
