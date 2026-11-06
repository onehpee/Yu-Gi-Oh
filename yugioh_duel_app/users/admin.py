from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import NewUser

class UserAdminConfig(UserAdmin):
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['-date_joined']
    list_display = ['username', 'email', 'first_name', 'last_name', 'date_joined', 'is_staff', 'is_active']

    fieldsets = (
        (None, {'fields': ('username', 'email', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None,
         {'classes':('wide',),
          'fields': ('username', 'email', 'first_name', 'last_name','password1', 'password2', 'is_active', 'is_staff',),}
         ),
    )

admin.site.register(NewUser, UserAdminConfig)
# admin.py — configures the admin dashboard
# Django provides a built-in admin interface where authorized users can manage application data.
# Register your models here.


