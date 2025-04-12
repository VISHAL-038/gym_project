from django.db import models
from django.conf import settings

class DailyProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    steps = models.PositiveIntegerField(default=0)
    calories = models.PositiveIntegerField(default=0)
    distance = models.FloatField(default=0.0)  # In kilometers

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.steps} steps"