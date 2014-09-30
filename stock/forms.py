from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=120)
    message = forms.CharField(widget=forms.Textarea())

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=120)
    email = forms.EmailField(max_length=120)
    password = forms.CharField(max_length=120, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=120, widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if User.objects.filter(username=username).exists():
            self._errors['username'] = ['User with such username already exists.']

        if User.objects.filter(email=email).exists():
            self._errors['email'] = ['User with such email already exists.']

        if password and password != password_confirmation:
            self._errors['password'] = ['Password does not match the confirm password.']

        return self.cleaned_data

