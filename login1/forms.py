from django import forms
from django.contrib.auth.hashers import make_password

from login1.models import Test


class formsdata(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('name', 'email', 'username', 'password')

    name = forms.CharField(
        max_length=100,
        label='name',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    email = forms.EmailField(
        label='email',

        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
    )

    username = forms.CharField(
        max_length=100,
        label='username',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    password = forms.CharField(
        max_length=100,
        label='password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )