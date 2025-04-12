from django.contrib import admin
from .models import WorkoutPlan, Exercise, Schedule

class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at')
    search_fields = ('name', 'description')
    fields = ('user', 'name', 'description', 'image', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'workout_plan', 'sets', 'reps', 'duration')
    list_filter = ('workout_plan',)
    search_fields = ('name', 'description')
    fields = ('workout_plan', 'name', 'sets', 'reps', 'duration', 'description', 'video')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'day_of_week', 'start_time')
    list_filter = ('day_of_week',)
    search_fields = ('exercise__name',)

admin.site.register(WorkoutPlan, WorkoutPlanAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Schedule, ScheduleAdmin)