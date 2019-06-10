from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')), # Used for logging into rest framework's browsable API
    path('api/', include('api.urls')),
    path('', include('testapp.urls')),
    path('admin/', admin.site.urls),
    # path('auth/', include('rest_framework_social_oauth2.urls')),
]
