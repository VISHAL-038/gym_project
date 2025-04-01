from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('book/<int:service_id>/', views.book_service, name='book_service'),
    path('get-time-slots/', views.get_time_slots, name='get_time_slots'),
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]