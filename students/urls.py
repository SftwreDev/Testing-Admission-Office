from django.urls import path

from .views import (
    student_profile,
)


app_name = 'students'

urlpatterns = [
    path('student-profile/', student_profile, name = 'student_profile'),
]
