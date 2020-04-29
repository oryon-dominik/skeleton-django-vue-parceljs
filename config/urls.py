""" base URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from .generic_views import ApplicationView

urlpatterns = [
    path('', ApplicationView.as_view(template_name='application.html')),
    path('', include('apps.users.urls', namespace="users")),
    path('admin/', admin.site.urls),
]
