from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^(\d+)$', 'blog.views.show', name='show'),
)
