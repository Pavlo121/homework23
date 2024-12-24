from django import forms
from .validators import validate_phone_number
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .widgets import Widget


class ContactForm(forms.Form):
    phone_number = forms.CharField(validators=[validate_phone_number])

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        return phone_number

class ContactForms(forms.Form):
    phone_number = forms.CharField(
        label="Ваш номер телефона",
        max_length=15
    )
    favorite_color = forms.ChoiceField(
        choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green')],
        widget=Widget(attrs={'data-custom': 'true'}),  # Передаем кастомный виджет
        label="Выберите ваш любимый цвет"
    )

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password',]

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Пароль должен быть не менее 8 символов.")
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Пароли не совпадают.")
        return confirm_password

