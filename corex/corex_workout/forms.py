from django import forms
from .models import WorkoutPlan, Exercise, Schedule

class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['name', 'description', 'image']  # Updated to include 'image' instead of 'video' and 'photo'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'sets', 'reps', 'duration', 'description', 'video']  # Updated to include 'video'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['day_of_week', 'start_time']
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
        }