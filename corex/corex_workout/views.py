from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WorkoutPlan, Exercise, Schedule
from .forms import WorkoutPlanForm, ExerciseForm, ScheduleForm

@login_required
def workout_plan_list(request):
    workout_plans = WorkoutPlan.objects.filter(user=request.user)
    return render(request, 'corex_workout/workout_plan_list.html', {'workout_plans': workout_plans})

@login_required
def workout_plan_create(request):
    if request.method == 'POST':
        form = WorkoutPlanForm(request.POST)
        if form.is_valid():
            workout_plan = form.save(commit=False)
            workout_plan.user = request.user
            workout_plan.save()
            return redirect('workout_plan_list')
    else:
        form = WorkoutPlanForm()
    return render(request, 'corex_workout/workout_plan_form.html', {'form': form})

@login_required
def workout_plan_detail(request, plan_id):
    workout_plan = get_object_or_404(WorkoutPlan, id=plan_id, user=request.user)
    return render(request, 'corex_workout/workout_plan_detail.html', {'workout_plan': workout_plan})

@login_required
def exercise_create(request, plan_id):
    workout_plan = get_object_or_404(WorkoutPlan, id=plan_id, user=request.user)
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.workout_plan = workout_plan
            exercise.save()
            return redirect('workout_plan_detail', plan_id=workout_plan.id)
    else:
        form = ExerciseForm()
    return render(request, 'corex_workout/exercise_form.html', {
        'form': form,
        'workout_plan': workout_plan
    })

@login_required
def schedule_create(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id, workout_plan__user=request.user)
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.exercise = exercise
            schedule.save()
            return redirect('workout_plan_detail', plan_id=exercise.workout_plan.id)
    else:
        form = ScheduleForm()
    return render(request, 'corex_workout/schedule_form.html', {
        'form': form,
        'exercise': exercise
    })