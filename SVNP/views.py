from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProjectForm
from .models import Project
from django.utils import timezone


def project_list(request):
    projects = Project.objects.order_by('-created_date')
    return render(request, 'SVNP/project_list.html', {'projects': projects})


def project_detail(request, pk):
    projects = get_object_or_404(Project, pk=pk)
    return render(request, 'SVNP/project_detail.html', {'projects': projects})


def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.created_date = timezone.now()
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'SVNP/project_edit.html', {'form': form})

