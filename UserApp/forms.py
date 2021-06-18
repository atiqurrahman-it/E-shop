from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SingUpCreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label="",
                             widget=forms.TextInput(attrs={'placeholder': 'Email ', 'type': 'email', }))

    password1 = forms.CharField(required=True,
                                label='',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True,
                                label='',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation'}))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
