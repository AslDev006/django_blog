from django import forms
from django.contrib.auth.forms import UserCreationForm

from AUTH.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class SignUpPage2Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'address', 'gender']