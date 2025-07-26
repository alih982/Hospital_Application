from django import forms
from django.contrib.auth.password_validation import validate_password

class RegisterForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self, password):
        password = self.cleaned_data['password']
        validate_password(password)
        return password