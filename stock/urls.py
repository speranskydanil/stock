from django.conf.urls import patterns, include, url

from django.views.generic.base import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/blog', permanent=False)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^about$', 'stock.views.about', name='about'),
    url(r'^contact$', 'stock.views.contact', name='contact'),
    url(r'^sign_in$', 'stock.views.sign_in', name='sign_in'),
    url(r'^sign_up$', 'stock.views.sign_up', name='sign_up'),
    url(r'^sign_out$', 'django.contrib.auth.views.logout', { 'next_page': '/' }, name='sign_out'),
)

