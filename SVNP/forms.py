from django import forms

from .models import User, Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('author', 'name', 'title', 'created_date')


class CreateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'second_name', 'age', 'password', 'role')
