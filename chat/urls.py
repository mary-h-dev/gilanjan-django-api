from django.urls import path ,include
from chat import admin
app_name = 'chat'


urlpatterns = [
    path('api/v1/',include('chat.api.v1.urls')),
]

