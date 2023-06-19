from rest_framework import permissions
from rest_framework.views import Request, View


class MoviesPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return bool(
            request.method in "GET" or
            request.user.is_employee
            )

class AuthenticatedMovie(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return bool(request.user and request.user.is_authenticated)
