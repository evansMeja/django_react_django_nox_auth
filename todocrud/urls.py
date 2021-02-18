"""
todocrud URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings



urlpatterns = [
    path('', include('frontend.urls')),
    path('api/', include('todos.api.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.api.urls')), 
]



