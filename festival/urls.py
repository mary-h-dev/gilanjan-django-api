from django.urls import path, include


app_name = "festival"

urlpatterns = [

    path('api/v1/',include('festival.api.v1.urls')),
]