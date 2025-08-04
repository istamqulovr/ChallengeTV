from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(required=True, label="Имя")
    last_name = forms.CharField(required=True, label="Фамилия")
    password1 = forms.CharField(required=True, label="пароль")
    password2 = forms.CharField(required=True, label="пароль 2")




    gender = forms.ChoiceField(
        choices=[('male', 'Мужской'), ('female', 'Женский')],
        widget=forms.RadioSelect,
        label="Пол"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2' ,'gender']

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if gender not in ['male', 'female']:
            raise forms.ValidationError("Выберите корректный пол.")
        return gender
