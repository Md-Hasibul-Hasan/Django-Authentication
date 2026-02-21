from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class UserModelAdmin(UserAdmin):
    model = User
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','email', 'name','is_active', 'is_superuser', 'is_staff','is_customer','is_seller', 'created_at', 'updated_at')
    list_filter = ('is_superuser',)
    fieldsets = [
        ("User Details", {'fields': ['email', 'password']}),
        ("Personal Details", {'fields': ['name','city']}),
        ("Permissions", {'fields': ['is_active','is_staff','is_superuser','is_customer','is_seller']}),
    ]

    add_fieldsets = [
        (
        None,
        {
            'classes': ('wide',),
            'fields': ('email','password1', 'password2'),
        },
        ),
    ]

    search_fields = ('email',)
    ordering = ('email','id',)
    filter_horizontal = ()

admin.site.register(User, UserModelAdmin)
