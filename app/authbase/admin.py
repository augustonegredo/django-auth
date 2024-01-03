from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser


class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ("email", "is_staff", "is_active", "usuario",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        ("Admin", {"fields": ("email", "password", "username", "usuario")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "username", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions", "usuario",
            )}
         ),
    )
    search_fields = ("username", "first_name", "last_name", "email", 'usuario',)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
