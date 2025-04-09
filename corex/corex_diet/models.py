from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    meals = models.ManyToManyField('Meal', blank=True)

    def __str__(self):
        return f"{self.user.username}'s Meal Plan for {self.date}"

class Meal(models.Model):
    name = models.CharField(max_length=100)
    preparation_time = models.PositiveIntegerField()  # In minutes
    calories = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dietary_category = models.CharField(max_length=50, choices=[
        ('all', 'All'),
        ('fat_loss', 'Fat Loss'),
        ('bulk', 'Bulk'),
        ('vegan', 'Vegan'),
    ], default='all')
    image = models.ImageField(upload_to='meals/', blank=True, null=True)  # New field for images

    def __str__(self):
        return self.name

class NutritionalInfo(models.Model):
    meal = models.OneToOneField(Meal, on_delete=models.CASCADE)
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()

    def __str__(self):
        return f"Nutrition for {self.meal.name}"

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title