from django.contrib import admin
from .models import WellnessService, TimeSlot, Booking

admin.site.register(WellnessService)
admin.site.register(TimeSlot)
admin.site.register(Booking)