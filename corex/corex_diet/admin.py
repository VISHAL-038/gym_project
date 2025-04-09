from django.contrib import admin
from .models import MealPlan, Meal, NutritionalInfo, Recipe

class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'meals_count')
    list_filter = ('date', 'user')
    search_fields = ('user__username',)

    def meals_count(self, obj):
        return obj.meals.count()
    meals_count.short_description = 'Number of Meals'

class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'preparation_time', 'calories', 'price', 'dietary_category', 'image')  # Added image
    list_filter = ('dietary_category',)
    search_fields = ('name', 'description')

class NutritionalInfoAdmin(admin.ModelAdmin):
    list_display = ('meal', 'protein', 'carbs', 'fat')
    search_fields = ('meal__name',)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'meal')
    search_fields = ('title', 'description')

admin.site.register(MealPlan, MealPlanAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(NutritionalInfo, NutritionalInfoAdmin)
admin.site.register(Recipe, RecipeAdmin)