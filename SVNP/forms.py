from django import forms
from .models import Project, CustomUser, File


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'title')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.Textarea(attrs={'class': 'form-control'}),
        }


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file_version', 'file_upload')

        widgets = {
            'file_version': forms.TextInput(attrs={'class': 'form-control'}),
            'file_upload': forms.FileInput(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'password', 'password2')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']
