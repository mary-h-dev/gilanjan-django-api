from django.urls import path, include


app_name = "food"

urlpatterns = [

    path('api/v1/',include('food.api.v1.urls')),
]