from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from users import views as user_views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')), # Used for logging into rest framework's browsable API
    path('api/', include('api.urls')),
    path('', include('testapp.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register)
]
