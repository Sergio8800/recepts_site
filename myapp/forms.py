import datetime
from urllib import request

import django.contrib.auth.forms
from django.contrib.auth.forms import UserCreationForm, User, AuthenticationForm
from django.utils.safestring import SafeString

from .models import *
from django import forms


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Login', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    # username = forms.CharField(max_length=50, label='Login', widget=forms.HiddenInput())
    password1 = forms.CharField(label='Password', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Password repeat', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    t_number = forms.CharField(max_length=15, label='phone namber')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 't_number')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=50, label='Login', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(label='Password', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=50)


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "not category"
        self.fields['name'].initial = 'entre new'
        # self.fields['username'].initial = User.get_username()
    class Meta:
        model = Recept
        # widgets = {
        #     "username": forms.HiddenInput(),
        #
        # }
        fields = '__all__'
        # fields = ['name', 'category', 'description']




