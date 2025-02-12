from django.urls import path, include


app_name = "tag"

urlpatterns = [

    path('api/v1/',include('tag.api.v1.urls')),
]