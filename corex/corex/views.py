from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from corex_diet.models import MealPlan, Meal
from corex_workout.models import WorkoutPlan
from corex_progress.models import DailyProgress

@login_required
def home(request):
    today = timezone.now().date()
    # Today's Workout
    workout = WorkoutPlan.objects.filter(user=request.user, created_at__date=today).first()
    if not workout:
        workout = WorkoutPlan.objects.filter(user=request.user).order_by('-created_at').first()
    # workout_duration = None
    # if workout and workout.duration:
    #     workout_duration = f"≈ {workout.duration // 60} hour{'s' if workout.duration // 60 != 1 else ''}" if workout.duration >= 60 else f"≈ {workout.duration} min"

    # Today's Diet Chart
    meal_plan = MealPlan.objects.filter(user=request.user, date=today).first()
    meals = meal_plan.meals.all() if meal_plan else []

    # Daily Progress
    daily_progress = DailyProgress.objects.filter(user=request.user, date=today).first()
    if not daily_progress:
        daily_progress = DailyProgress.objects.create(user=request.user, steps=0, calories=0, distance=0.0)
    progress = {
        'steps': daily_progress.steps,
        'calories': daily_progress.calories,
        'distance': daily_progress.distance,
        'walk_run_distance': daily_progress.distance,
    }

    context = {
        'workout': workout,
        # 'workout_duration': workout_duration,
        'meal_plan': meal_plan,
        'meals': meals,
        'progress': progress,
        'user': request.user,
    }
    return render(request, 'home.html', context)

@login_required
def profile(request):
    today = timezone.now().date()
    daily_progress = DailyProgress.objects.filter(user=request.user, date=today).first()
    if not daily_progress:
        daily_progress = DailyProgress.objects.create(user=request.user, steps=0, calories=0, distance=0.0)
    progress = {
        'steps': daily_progress.steps,
        'calories': daily_progress.calories,
        'distance': daily_progress.distance,
        'walk_run_distance': daily_progress.distance,
    }

    context = {
        'progress': progress,
        'user': request.user,
    }
    return render(request, 'corex/profile.html', context)

@login_required
def update_progress(request):
    if request.method == 'POST':
        today = timezone.now().date()
        daily_progress = DailyProgress.objects.filter(user=request.user, date=today).first()
        if not daily_progress:
            daily_progress = DailyProgress.objects.create(user=request.user, steps=0, calories=0, distance=0.0)
        daily_progress.steps = request.POST.get('steps', 0)
        daily_progress.calories = request.POST.get('calories', 0)
        daily_progress.distance = request.POST.get('distance', 0.0)
        daily_progress.save()
        messages.success(request, "Progress updated successfully!")
        return redirect('home')
    return redirect('home')