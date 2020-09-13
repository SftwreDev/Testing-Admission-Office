from django.shortcuts import render, redirect,get_object_or_404

from django.views.generic import ListView
from .models import FileUpload
from .forms import FileUploadForm


def FileList(request):
    template_name = 'repository/file_list.html'
    files = FileUpload.objects.all()
    form = FileUploadForm(request.POST or None)
    if request.method == 'POST':
        form = FileUploadForm(request.POST , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("documents:list_of_files")

    context = {
            'files' : files,
            'form' : form
        }

    return render(request, template_name, context)


def delete_file(request, pk):
    template_name = 'repository/file_list.html'

    obj = get_object_or_404(FileUpload, pk = pk)
    if request.method == 'POST':
        obj = get_object_or_404(FileUpload, pk = pk)
        obj.delete()

        return redirect("documents:list_of_files")

    return render(request, template_name, {
        'obj' : obj,
    })



