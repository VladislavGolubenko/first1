from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=250,
        label='логин'
    )
    password = forms.CharField(
        label='пароль',
        widget=forms.PasswordInput()
    )

    class Meta:
        models = User
        fields = ('username', 'password')


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        max_length=250,
        label='Имя'
    )

    last_name = forms.CharField(
        max_length=250,
        label='Фамилия'
    )

    email = forms.EmailField(
        label='email',
    )

    username = forms.CharField(
        max_length=250,
        label='Имя используемое при авторизации'
    )

    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']