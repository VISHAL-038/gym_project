from django import forms
from .models import WellnessService, TimeSlot

class BookingForm(forms.Form):
    service = forms.ModelChoiceField(queryset=WellnessService.objects.all(), label="Select Service")
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Select Date")
    time_slot = forms.ModelChoiceField(queryset=TimeSlot.objects.none(), label="Select Time Slot")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'service' in self.data:
            try:
                service_id = int(self.data.get('service'))
                date = self.data.get('date')
                if date:
                    self.fields['time_slot'].queryset = TimeSlot.objects.filter(
                        service_id=service_id, date=date, is_booked=False
                    )
            except (ValueError, TypeError):
                pass
        elif self.initial.get('service'):
            self.fields['time_slot'].queryset = TimeSlot.objects.filter(
                service=self.initial['service'], is_booked=False
            )