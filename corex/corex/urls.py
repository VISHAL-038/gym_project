"""
URL configuration for corex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf import settings
from django.conf.urls.static import static
from .views import home, profile, update_progress

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('update_progress/', update_progress, name='update_progress'),
    path('explore/', home, name='explore'),  # Placeholder
    path('cart/', include('corex_order.urls')),  # Placeholder
    path('diet/', include('corex_diet.urls')),
    path('user/', include('corex_user.urls')),
    path('booking/', include('corex_booking.urls')),
    path('workout/', include('corex_workout.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)