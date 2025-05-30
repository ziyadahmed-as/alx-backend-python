from django.contrib import admin
from django.urls import path, include
from .models import User, Conversation, Message
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    """Define admin model for custom User model with no email field."""
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
admin.site.register(User, UserAdmin)
admin.site.register(Conversation)
admin.site.register(Message)
# Register your models here.
