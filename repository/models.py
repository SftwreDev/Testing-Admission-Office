from django.db import models

# Create your models here.
class FileUpload(models.Model):
    date = models.DateTimeField(auto_now_add= True)
    name = models.CharField(max_length=100, verbose_name="Document's Name")
    document = models.FileField(upload_to='documents')
    complete = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    