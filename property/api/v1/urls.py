from django.urls import path
from .views import (
    PropertiesListView,
    PropertyDetailView,
    PropertyReservationsView,
    CreatePropertyView,
    BookPropertyView,
    ToggleFavoriteView,
)

urlpatterns = [
    path('', PropertiesListView.as_view(), name='api_properties_list'),
    path('create/', CreatePropertyView.as_view(), name='api_create_property'),
    path('<uuid:pk>/', PropertyDetailView.as_view(), name='api_properties_detail'),
    path('<uuid:pk>/book/', BookPropertyView.as_view(), name='api_book_property'),
    path('<uuid:pk>/reservations/', PropertyReservationsView.as_view(), name='api_property_reservations'),
    path('<uuid:pk>/toggle_favorite/', ToggleFavoriteView.as_view(), name='api_toggle_favorite'),
]
