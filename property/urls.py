from django.urls import path ,include
from property import admin
app_name = 'property'


urlpatterns = [
    path('api/v1/',include('property.api.v1.urls')),
]

