from rest_framework import permissions

class IsAdminEmployeeOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow admin employees to perform CRUD operations,
    while allowing read-only access for others.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # Check if the user has the 'admin employee' role
            return request.user.userprofile.role.name == 'admin employee'
        return False

class IsEmployeeOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow employees (both normal and admin) to perform CRUD operations,
    while allowing read-only access for others.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            role = request.user.userprofile.role.name
            return role in ['employee', 'admin employee']
        return False
