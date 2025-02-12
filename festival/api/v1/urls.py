from django.urls import path
from .views import (
    FestivalCreateView, FestivalListView, FestivalDetailView,
    FestivalUpdateView, FestivalDeleteView
)

urlpatterns = [
    path('ft/', FestivalListView.as_view(), name='festival-list'),
    path('ft/create/', FestivalCreateView.as_view(), name='festival-create'),
    path('ft/<slug:slug>/', FestivalDetailView.as_view(), name='festival-detail'),
    path('ft/<slug:slug>/update/', FestivalUpdateView.as_view(), name='festival-update'),
    path('ft/<slug:slug>/delete/', FestivalDeleteView.as_view(), name='festival-delete'),
]
