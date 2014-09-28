from django.shortcuts import render
from blog.models import Article

def index(request):
    articles = Article.objects.select_related().all()
    return render(request, 'blog/index.html', { 'articles': articles })

