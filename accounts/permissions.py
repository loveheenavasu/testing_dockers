from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        is_not_super_user = (False if request.user.is_superuser else True)
        return bool(request.user and request.user.is_staff and is_not_super_user)


# class IsSuperUser(BasePermission):
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_superuser)

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)


class IsUser(BasePermission):
    def has_permission(self, request, view):
        is_not_super_user = (False if request.user.is_superuser else True)
        is_not_staff = (False if request.user.is_staff else True)
        return bool(request.user.is_authenticated and is_not_super_user and is_not_staff)


class IsGeneralManager(BasePermission):
    def has_permission(self, request, view):
        is_not_super_user = (False if request.user.is_superuser else True)
        is_general_manager = (True if ((request.user.is_general_manager and request.user.is_admin) or
                                       request.user.is_general_manager) else False)
        return bool(request.user.is_authenticated and is_not_super_user and is_general_manager)