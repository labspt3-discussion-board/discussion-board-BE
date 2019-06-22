from rest_framework import permissions
from django.conf import settings

class IsCreator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print('>')
        print(request.user)
        print(obj.owner)
        print('^')
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user

class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print('>')
        print(request.user.id)
        print(obj.id)
        print('^')
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
