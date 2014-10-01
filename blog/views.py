from stock.imports import *

_render = render

def render(request, template, context):
    context['categories'] = Category.objects.select_related().all()
    context['recent_articles'] = Article.objects.select_related().all()[:7]
    context['location'] = 'blog'
    return _render(request, template, context)

@require_GET
def index(request):
    articles = paginated(Article.objects.select_related().all(), request)
    return render(request, 'blog/index.html', { 'articles': articles })

@require_GET
def show(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'blog/show.html', { 'article': article })

@login_required
def new(request, category = None):
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save()
            article.author = request.user
            article.save()
            messages.info(request, 'The article is created.')
            return redirect('blog:show', article.id)
    else:
        form = ArticleForm(initial={ 'category': category })

    return render(request, 'blog/new.html', { 'form': form })

@login_required
def edit(request, id):
    article = get_object_or_404(Article, pk=id)

    if article.author != request.user:
        return redirect('blog:index')

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            messages.info(request, 'The article is updated.')
            return redirect('blog:show', article.id)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'blog/edit.html', { 'form': form })

@require_GET
def show_category(request, id):
    category = get_object_or_404(Category, pk=id)
    articles = paginated(category.article_set.all(), request)
    return render(request, 'blog/show_category.html', { 'category': category, 'articles': articles })

