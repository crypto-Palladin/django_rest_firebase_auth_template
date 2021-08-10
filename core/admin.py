from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from core import models


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = models.CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'is_admin',
                    'first_name', 'last_name')
    list_filter = ('email', 'is_staff', 'is_admin', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_admin', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff',
                       'is_active', 'is_admin',
                       'first_name', 'last_name')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(models.CustomUser, CustomUserAdmin)
