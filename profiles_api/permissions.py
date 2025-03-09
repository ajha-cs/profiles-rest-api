from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""
    
    #called every time a request is made to the api
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        #Rules
        #Safe methods - reading object - GET Request -> or create a new object
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #Otherwise check whther the user is trying to update their own profile   
        return obj.id == request.user.id
        