from django import forms

from .models import User


class CreateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'second_name', 'age', 'password', 'role')
