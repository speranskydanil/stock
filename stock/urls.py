from django.conf.urls import patterns, include, url

from django.views.generic.base import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about$', 'stock.views.about', name='about'),
    url(r'^contact$', 'stock.views.contact', name='contact'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^$', RedirectView.as_view(url='/blog', permanent=False)),
)
