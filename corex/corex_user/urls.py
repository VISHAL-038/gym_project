from django.urls import path
from . import views

urlpatterns = [
    path('register/step1/', views.register_step1, name='register_step1'),
    path('register/step2/', views.register_step2, name='register_step2'),
    path('register/step3/', views.register_step3, name='register_step3'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
]