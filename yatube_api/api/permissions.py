from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """
    Чтение — всем (даже анонимам).
    Создание, изменение, удаление — только авторизованным пользователям.
    Изменение/удаление — только автору объекта.
    """

    def has_permission(self, request, view):
        """Проверка перед созданием объекта (POST)"""
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Проверка для уже существующего объекта"""
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
