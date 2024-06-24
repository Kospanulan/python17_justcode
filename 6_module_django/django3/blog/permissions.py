from rest_framework.permissions import BasePermission, DjangoModelPermissions

"""
    add_()
    delete_()
    change_()
    view_()

"""


class DjangoModelPermissionsWithRead(DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class IsUser2(BasePermission):
    """
    Allows access only to user2
    """

    def has_permission(self, request, view):
        print("is user2 check")
        return bool(request.user.username == 'user2')


class IsAdmin(BasePermission):
    """
    Allows access only to admin
    """

    def has_permission(self, request, view):
        print("is admin check")

        return bool(request.user.username == 'admin')