from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import WellnessService, TimeSlot, Booking



def service_list(request):
    services = WellnessService.objects.all()
    return render(request, 'corex_booking/service_list.html', {'services': services})

@login_required
def book_service(request, service_id):
    from .forms import BookingForm  # Move the import here
    service = get_object_or_404(WellnessService, id=service_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, initial={'service': service})
        if form.is_valid():
            time_slot = form.cleaned_data['time_slot']
            # Check if the time slot is still available
            if time_slot.is_booked:
                form.add_error(None, "This time slot is no longer available.")
            else:
                # Create the booking
                booking = Booking.objects.create(
                    user=request.user,
                    time_slot=time_slot,
                    status='Confirmed'
                )
                # Mark the time slot as booked
                time_slot.is_booked = True
                time_slot.save()
                return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm(initial={'service': service})
    return render(request, 'corex_booking/book_service.html', {
        'form': form,
        'service': service,
        'selected_date': request.POST.get('date') if request.method == 'POST' else None
    })

def get_time_slots(request):
    service_id = request.GET.get('service_id')
    date = request.GET.get('date')
    if service_id and date:
        time_slots = TimeSlot.objects.filter(
            service_id=service_id,
            date=date,
            is_booked=False
        ).values('id', 'start_time')
        time_slots_list = [
            {'id': slot['id'], 'start_time': slot['start_time'].strftime('%H:%M')}
            for slot in time_slots
        ]
        return JsonResponse({'time_slots': time_slots_list})
    return JsonResponse({'time_slots': []})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'corex_booking/booking_confirmation.html', {'booking': booking})