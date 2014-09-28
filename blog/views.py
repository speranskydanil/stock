from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Article

@require_GET
def index(request):
    articles = Article.objects.select_related().all()
    page = request.GET.get('page')
    paginator = Paginator(articles, 20)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', { 'articles': articles })

@require_GET
def show(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'blog/show.html', { 'article': article })

