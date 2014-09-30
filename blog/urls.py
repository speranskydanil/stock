from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'index', name='index'),
    url(r'^(\d+)$', 'show', name='show'),
    url(r'^new$', 'new', name='new'),
    url(r'^category/(\d+)/new$', 'new', name='new'),
    url(r'^category/(\d+)$', 'show_category', name='show_category'),
)
