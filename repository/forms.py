from django import forms

from . models import FileUpload, OfficeDocuments


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ('name', 'document', 'complete')


class OfficeFileUploadForm(forms.ModelForm):
    class Meta:
        model = OfficeDocuments
        fields = ('name', 'document')