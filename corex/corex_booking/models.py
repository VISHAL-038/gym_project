from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class WellnessService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()  # Duration in minutes
    image_url = models.URLField(max_length=200, null=True, blank=True)  # Changed from ImageField to URLField

    def __str__(self):
        return self.name

class TimeSlot(models.Model):
    service = models.ForeignKey(WellnessService, on_delete=models.CASCADE, related_name='time_slots')
    date = models.DateField()
    start_time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.service.name} - {self.date} {self.start_time}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name='bookings')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ], default='Pending')

    def __str__(self):
        return f"Booking by {self.user.username} for {self.time_slot}"