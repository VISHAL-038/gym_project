from django.contrib import admin
from .models import WorkoutPlan, Exercise, Schedule

# Optionally, customize the admin interface
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'updated_at')  # Fields to display in the list view
    list_filter = ('user', 'created_at')  # Filters for the sidebar
    search_fields = ('name', 'description')  # Searchable fields

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'workout_plan', 'sets', 'reps', 'duration')
    list_filter = ('workout_plan',)
    search_fields = ('name', 'description')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'day_of_week', 'start_time')
    list_filter = ('day_of_week',)
    search_fields = ('exercise__name',)

# Register the models with their admin classes
admin.site.register(WorkoutPlan, WorkoutPlanAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Schedule, ScheduleAdmin)