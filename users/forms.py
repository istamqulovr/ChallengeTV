from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(required=True, label="Имя")
    last_name = forms.CharField(required=True, label="Фамилия")
    gender = forms.ChoiceField(
        choices=[('male', 'Мужской'), ('female', 'Женский')],
        widget=forms.RadioSelect,
        label="Пол"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'password1', 'password2']
