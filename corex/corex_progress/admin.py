from django.contrib import admin
from .models import DailyProgress

@admin.register(DailyProgress)
class DailyProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'steps', 'calories', 'distance')
    list_filter = ('date',)
    search_fields = ('user__username',)