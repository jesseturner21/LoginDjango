from django import forms
from .models import User 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, required=True)
    phonenumber = forms.CharField(required=True)

    def clean(self):
        cleaned_data = super().clean()

        # Extract passwords
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        # Check if passwords match
        if password1 and password2 and password1 != password2:
            self.add_error("password2", "The two password fields must match.")

        # Check for existing username
        username = cleaned_data.get("username")
        if username and User.objects.filter(username=username).exists():
            self.add_error("username", "A user with that username already exists.")

        # Return data after validation
        return cleaned_data