from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Blogs

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_pic',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Blogs)