from django.contrib.auth.models import User  # Import the User model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from captcha.fields import CaptchaField


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='email')
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
