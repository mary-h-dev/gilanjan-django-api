from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# # تنظیمات Swagger
# schema_view = get_schema_view(
#     openapi.Info(
#         title="safarman api",
#         default_version='v1',
#         description="Description of your API",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="e.maryamhabibpour@gmail.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('useraccount/', include('useraccount.urls')),
    path('properties/', include('property.urls')),
    path('chat/', include('chat.urls')),
    path('blog/', include('blog.urls')),
    path('tags/', include('tag.urls')),
    path('food/', include('food.urls')),
    path('festival/', include('festival.urls')),
    path('photos/', include('photos.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    # مسیرهای Swagger
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('swagger/output.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

