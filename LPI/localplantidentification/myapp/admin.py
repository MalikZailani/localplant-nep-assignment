from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Extend the default UserAdmin class
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')

# Unregister the original User model
admin.site.unregister(User)

# Register the User model with the customized admin class
admin.site.register(User, CustomUserAdmin)

# Register your models here.
