from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.views.generic import ListView
from .models import FileUpload, OfficeDocuments
from .forms import FileUploadForm, OfficeFileUploadForm

@login_required
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


def office_file_list(request):
    template_name = "repository/office_file_list.html"

    file = OfficeDocuments.objects.all()
    form = OfficeFileUploadForm(request.POST or None , request.FILES or None)

    if request.method == 'POST':
        form = OfficeFileUploadForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
            return redirect('documents:office_file_list')
        else:
            messages.error(request, "Invalid input")
            form = OfficeFileUploadForm(request.POST or None , request.FILES or None)

    context = {'file':file, 'form':form}

    return render(request, template_name, context)

def office_file_update(request, pk):
    template_name = "repository/office_file_update.html"

    file = OfficeDocuments.objects.get(id=pk)
    form = OfficeFileUploadForm(request.POST or None , request.FILES or None, instance=file)

    if request.method == 'POST':
        form = OfficeFileUploadForm(request.POST or None , request.FILES or None, instance=file)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
            return redirect('documents:office_file_list')
        else:
            messages.error(request, "Invalid input")
            form = OfficeFileUploadForm(request.POST or None , request.FILES or None, instance=file)

    context = {'file':file, 'form':form}

    return render(request, template_name, context)
 
def office_file_delete(request, pk):
    

    file = OfficeDocuments.objects.get(id=pk)
    file.delete()
    return redirect('documents:office_file_list')
 