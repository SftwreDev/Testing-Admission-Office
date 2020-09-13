from django import forms

from . models import FileUpload


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        exclude = ('completed',)
        fields = ('name', 'document')