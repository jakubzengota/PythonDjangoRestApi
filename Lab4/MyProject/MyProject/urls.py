from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='My Project Swagger')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api_basic.urls')),
    path('', schema_view)
]
