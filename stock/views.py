from stock.imports import *

@require_GET
def about(request):
    return render(request, 'about.html', { 'location': 'about' })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            Message.objects.create(subject=form.cleaned_data['subject'], message=form.cleaned_data['message'])
            messages.info(request, 'The message is sent.')
            return redirect('blog:index')
    else:
        form = ContactForm()

    return render(request, 'contact.html', { 'form': form, 'location': 'contact' })

def sign_in(request):
    response = login(request, template_name='registration/sign_in.html')

    if request.user.is_authenticated():
        messages.info(request, 'You are signed in.')

    return response

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            User.objects.create_user(username, email, password)

            login(request, authenticate(username=username, password=password))

            messages.info(request, 'You are signed up.')
            return redirect('blog:index')
    else:
        form = SignUpForm()

    return render(request, 'registration/sign_up.html', { 'form': form })

@require_GET
@login_required
def profile(request):
    articles = paginated(Article.objects.select_related().filter(author=request.user), request)
    return render(request, 'profile.html', { 'articles': articles })

@require_GET
def user_profile(request, id):
    user = User.objects.get(id=id)
    articles = paginated(Article.objects.select_related().filter(author=user), request)
    return render(request, 'user_profile.html', { 'user': user, 'articles': articles })

