from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'height', 'weight', 'age', 'gender', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'gender')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('height', 'weight', 'age', 'fitness_goals', 'gender'),
        }),
    )
    search_fields = ('username', 'email')