import django_filters

from .models import StudentProfile

class StudentProfileFilter(django_filters.FilterSet):
    class Meta:
        model = StudentProfile
        fields = ['l_name', 'f_name', 'm_name', 'major', 'college', 'course', 'yearlevel']
