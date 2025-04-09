from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import MealPlan, Meal, Recipe
from django.db.models import Q

@login_required
def diet_home(request):
    today = timezone.now().date()
    meal_plan, created = MealPlan.objects.get_or_create(user=request.user, date=today)
    meals = meal_plan.meals.all()
    return render(request, 'corex_diet/diet_home.html', {'meals': meals, 'today': today})

@login_required
def diet_tracking(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', 'all')
    meals = Meal.objects.all()
    if query:
        meals = meals.filter(Q(name__icontains=query))
    if category != 'all':
        meals = meals.filter(dietary_category=category)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        preparation_time = request.POST.get('preparation_time')
        calories = request.POST.get('calories')
        price = request.POST.get('price')
        dietary_category = request.POST.get('dietary_category')
        image = request.FILES.get('image')  # New field for image upload
        if name and preparation_time and calories and price and dietary_category:
            meal = Meal.objects.create(
                name=name,
                preparation_time=preparation_time,
                calories=calories,
                price=price,
                dietary_category=dietary_category,
                image=image
            )
            # Optionally add nutritional info or link to meal plan here
    return render(request, 'corex_diet/diet_tracking.html', {'meals': meals, 'query': query, 'category': category})

@login_required
def recipe_guidance(request):
    recipes = Recipe.objects.all()  # Or filter by meal if linked
    return render(request, 'corex_diet/recipe_guidance.html', {'recipes': recipes})