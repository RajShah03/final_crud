
from django.urls import path
from .views import employee_form  # Import the view

urlpatterns = [
    path('insert/', employee_form, name='insert'),  # Use snake_case for URL name
]
