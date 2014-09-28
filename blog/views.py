from django.shortcuts import render
from django.views.decorators.http import require_GET
from blog.models import Article

@require_GET
def index(request):
    articles = Article.objects.select_related().all()
    return render(request, 'blog/index.html', { 'articles': articles })

@require_GET
def show(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'blog/show.html', { 'article': article })

