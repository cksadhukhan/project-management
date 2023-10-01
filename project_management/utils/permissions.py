from rest_framework import permissions

from task.models import Task

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin'

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'manager'

class IsMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'member'
    
class IsTaskManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        task_id = view.kwargs.get('pk')
        if task_id is not None:
            try:
                task = Task.objects.get(pk=task_id)
                return request.user == task.assignee
            except Task.DoesNotExist:
                pass
        return False