from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.order_by('-created_date')
    return render(request, 'SVNP/project_list.html', {'projects': projects})

