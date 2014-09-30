from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Article, Category
from blog.forms import ArticleForm

_render = render

def render(request, template, context):
    context['categories'] = Category.objects.select_related().all()
    context['recent_articles'] = Article.objects.select_related().all()[:7]
    context['location'] = 'blog'
    return _render(request, template, context)

def paginated(objects, request):
    paginator = Paginator(objects, 20)
    page = request.GET.get('page')

    try:
        return paginator.page(page)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)

@require_GET
def index(request):
    articles = paginated(Article.objects.select_related().all(), request)
    return render(request, 'blog/index.html', { 'articles': articles })

@require_GET
def show(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'blog/show.html', { 'article': article })

@login_required
def new(request, category = None):
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save()
            messages.info(request, 'The article is created.')
            return redirect('blog:show', article.id)
    else:
        form = ArticleForm(initial={ 'category': category })

    return render(request, 'blog/new.html', { 'form': form })

@require_GET
def show_category(request, id):
    category = Category.objects.get(id=id)
    articles = paginated(category.article_set.all(), request)
    return render(request, 'blog/show_category.html', { 'category': category, 'articles': articles })

