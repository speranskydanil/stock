from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=120, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    message = forms.CharField(widget=forms.Textarea(attrs={ 'class': 'form-control' }))

