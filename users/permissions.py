from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    # def has_permission(self, request, view):
    #     print(view.get_object(author))
    #     return request.user == view.get_object().user

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user