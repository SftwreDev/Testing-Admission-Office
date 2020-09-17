from django.db import models

# Create your models here.

class Campus(models.Model):
    campus = models.CharField(max_length=100, verbose_name='Campus')

    def __str__(self):
        return self.campus
    
class College(models.Model):
    college = models.CharField(max_length=100, verbose_name='College')

    def __str__(self):
        return self.college

class Course(models.Model):
    course = models.CharField(max_length=100, verbose_name='Course')

    def __str__(self):
        return self.course
        
class Major(models.Model):
    major = models.CharField(max_length=100, verbose_name='Major')

    def __str__(self):
        return self.major

class StudentProfile(models.Model):
    year_level = (
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', 'Third'),
        ('Fourth', 'Fourth')
    )
    complete = (
        ('completed' , 'completed'),
        ('incomplete' , 'incomplete')
    )
    f_name = models.CharField(max_length=100, verbose_name='First Name')
    l_name = models.CharField(max_length=100, verbose_name='Last Name')
    m_name = models.CharField(max_length=100, blank=True, verbose_name='Middle Name')
    college = models.ForeignKey(College, on_delete=models.CASCADE, verbose_name='College')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course')
    major = models.ForeignKey(Major, on_delete=models.CASCADE, verbose_name = 'Major')
    yearlevel = models.CharField(max_length=100, choices=year_level, verbose_name='Year Level')
    completed = models.CharField(max_length=100, choices=complete, verbose_name='Status')
    def __str__(self):
        return self.l_name +  ',' + self.f_name + " " +self.m_name
    
