from rest_framework import permissions


class IsAdminUserOrElseReadOnly(permissions.BasePermission):

    # 每次请求到来时，被唤醒执行
    def has_permission(self, request, view):
        
        # 安全操作所有人都可以执行
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_superuser