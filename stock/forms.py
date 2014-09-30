from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=120, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    message = forms.CharField(widget=forms.Textarea(attrs={ 'class': 'form-control' }))

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=120, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    email = forms.EmailField(max_length=120, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    password = forms.CharField(max_length=120, widget=forms.PasswordInput(attrs={ 'class': 'form-control' }))
    password_confirmation = forms.CharField(max_length=120, widget=forms.PasswordInput(attrs={ 'class': 'form-control' }))

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

