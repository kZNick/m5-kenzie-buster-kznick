from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class Authenticated(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return bool(
            request.method in "POST" or request.user and request.user.is_authenticated
        )

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user: User) -> bool:
        return bool(request.user.is_employee or request.user.id == user.id)