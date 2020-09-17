from django.contrib import admin

from .models import Campus, College, Course, Major, StudentProfile

admin.site.register(Campus)
admin.site.register(College)
admin.site.register(Course)
admin.site.register(Major)
admin.site.register(StudentProfile)