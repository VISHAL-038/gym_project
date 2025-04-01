from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    height = models.FloatField(null=True, blank=True)  # Height in cm
    weight = models.FloatField(null=True, blank=True)  # Weight in kg
    age = models.PositiveIntegerField(null=True, blank=True)
    fitness_goals = models.JSONField(null=True, blank=True)  # Store as a list of goals
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True, blank=True)

    def __str__(self):
        return self.username