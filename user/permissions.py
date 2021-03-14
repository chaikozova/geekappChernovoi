from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        try:
            return bool(request.user.is_staff)
        except:
            raise PermissionDenied({'detail': "You do not have permission to perform this action."})


class IsTecher(BasePermission):

    def has_permission(self, request, view):
        try:
            return bool(request.user.user_type == 2)
        except:
            raise  PermissionDenied({'detail': "You do not have permission to perform this action."})


class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS