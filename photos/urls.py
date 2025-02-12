from django.urls import path, include


app_name = "photos"

urlpatterns = [

    path('api/v1/',include('photos.api.v1.urls')),
]