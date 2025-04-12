from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plans')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='workouts/images/', blank=True, null=True)  # Workout plan image

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class Exercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)
    sets = models.IntegerField(default=3)
    reps = models.IntegerField(default=10)
    duration = models.IntegerField(blank=True, null=True)  # Duration in minutes (optional)
    description = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='workouts/videos/', blank=True, null=True)  # Exercise video

    def __str__(self):
        return f"{self.name} - {self.workout_plan.name}"

class Schedule(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])
    start_time = models.TimeField()

    def __str__(self):
        return f"{self.exercise.name} on {self.day_of_week} at {self.start_time}"