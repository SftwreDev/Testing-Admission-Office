from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CampusForm, CollegeForm, MajorForm, CourseForm, StudentProfileForm
from .models import Campus, College, Course, Major, StudentProfile
from .filters import StudentProfileFilter

@login_required
def student_profile(request):
    template = 'students/student_profile.html'
    student_list = StudentProfile.objects.all()
    student_form = StudentProfileForm(request.POST or None)
    filter_qs = StudentProfileFilter(request.GET, queryset=student_list)

    if request.method == 'POST':
        student_form = StudentProfileForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return redirect('students:student_profile')
        else:
            student_form = StudentProfileForm(request.POST or None)

    context = {
        'student_form' : student_form,
        'student_list' : student_list,
        'filter_qs' : filter_qs ,
    }
    return render(request, template, context)
            
