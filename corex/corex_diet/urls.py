from django.urls import path
from . import views

urlpatterns = [
    path('', views.diet_home, name='diet_home'),
    path('tracking/', views.diet_tracking, name='diet_tracking'),
    path('recipes/', views.recipe_guidance, name='recipe_guidance'),
]