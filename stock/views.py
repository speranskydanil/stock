from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from django.contrib import messages
from stock.forms import ContactForm
from stock.models import Message

@require_GET
def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            Message.objects.create(subject=form.cleaned_data['subject'], message=form.cleaned_data['message'])
            messages.info(request, 'The message is sent.')
            return redirect('blog:index')

    else:
        form = ContactForm()

    return render(request, 'contact.html', { 'form': form })

