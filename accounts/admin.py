from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomBaseUser


class CustomUserAdmin(UserAdmin):
    model = CustomBaseUser
    list_display = ('email','username','address', 'is_staff', 'is_admin',)
    search_fields = ('email', 'username')
    readonly_fields = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(CustomBaseUser, CustomUserAdmin)