from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from corex_diet.models import MealPlan, Meal
from corex_workout.models import WorkoutPlan

@login_required
def home(request):
    today = timezone.now().date()
    # Today's Workout (latest for the user, prioritized by today)
    workout = WorkoutPlan.objects.filter(user=request.user, created_at__date=today).first()
    if not workout:
        workout = WorkoutPlan.objects.filter(user=request.user).order_by('-created_at').first()

    # Format workout duration in hours if it exists
    # workout_duration = None
    # if workout and workout.duration:
    #     workout_duration = f"≈ {workout.duration // 60} hour{'s' if workout.duration // 60 != 1 else ''}" if workout.duration >= 60 else f"≈ {workout.duration} min"

    # Today's Diet Chart (latest MealPlan for today)
    meal_plan = MealPlan.objects.filter(user=request.user, date=today).first()
    meals = meal_plan.meals.all() if meal_plan else []

    # Daily Progress (simulated data; replace with actual tracking if implemented)
    progress = {
        'steps': 250,  # Example value (out of 10000)
        'calories': 250,  # Example value in Kcal
        'distance': 2,  # Example value in Km
        'walk_run_distance': 0.0,  # Example value in Km
    }

    context = {
        'workout': workout,
        # 'workout_duration': workout_duration,  # Pass formatted duration
        'meal_plan': meal_plan,
        'meals': meals,
        'progress': progress,
        'user': request.user,
    }
    return render(request, 'home.html',context)