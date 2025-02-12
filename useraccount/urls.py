from django.urls import path ,include
from useraccount import admin
app_name = 'useraccount'


urlpatterns = [
    path('api/v1/',include('useraccount.api.v1.urls')),
]

