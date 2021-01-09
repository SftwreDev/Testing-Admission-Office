from django.db import models
from students.models import StudentProfile
from django.contrib.auth.models import User

# Create your models here.
class FileUpload(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add= True)
    name = models.CharField(max_length=100, verbose_name="Document's Name")
    document = models.FileField(upload_to='documents')
    complete = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class OfficeDocuments(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add= True)
    name = models.CharField(max_length=100, verbose_name="Document's Name")
    document = models.FileField(upload_to='documents')

    def __str__(self):
        return self.name