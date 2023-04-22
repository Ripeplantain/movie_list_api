from rest_framework import permissions


# class AdminorReadOnly(permissions.IsAdminUser):
    
#     def has_permission(self, request, view):
#         admin_permission = bool(request.user and request.user.is_staff)
#         return request.method == "GET" or admin_permission



class ReviewUserorReadOnly(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            #means they only trying to access the data
            return True
        else:
            #they are trying to alter the data
            return obj.review_user == request.user