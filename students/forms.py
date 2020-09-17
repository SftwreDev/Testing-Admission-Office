from django import forms

from .models import Campus, College, Course, Major, StudentProfile


class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = '__all__'

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class MajorForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = '__all__'

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = '__all__'