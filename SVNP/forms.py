from django import forms
from .models import Project, CustomUser


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('author', 'name', 'title', 'created_date')


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "myfield"}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={"class": "myfield"}))
    required_css_class = "formStyles"

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'role')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
