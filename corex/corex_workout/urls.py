from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_plan_list, name='workout_plan_list'),
    path('create/', views.workout_plan_create, name='workout_plan_create'),
    path('<int:plan_id>/', views.workout_plan_detail, name='workout_plan_detail'),
    path('<int:plan_id>/exercise/create/', views.exercise_create, name='exercise_create'),
    path('exercise/<int:exercise_id>/schedule/create/', views.schedule_create, name='schedule_create'),
]