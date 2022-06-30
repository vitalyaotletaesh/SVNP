from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import svn_commands_script
from .forms import UserRegistrationForm, LoginForm, FileUploadForm
from .forms import ProjectForm
from .models import Project, File
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


def file_data(request):
    files = File.objects.order_by('file_version')
    return render(request, 'SVNP/project_detail.html', {'files': files})


def file_upload(request):
    if request.method == 'POST':
        file = FileUploadForm(request.POST, request.FILES)
        if file.is_valid():
            file.save()
            svn_commands_script.svn_commit()
            return redirect('project_list')

    else:
        file = FileUploadForm()
    return render(request, 'SVNP/file_upload.html', {'file': file})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('project_list')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login or password')
    else:
        form = LoginForm()
    return render(request, 'SVNP/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'SVNP/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'SVNP/register.html', {'user_form': user_form})

