from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'project.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', "acorta.views.barra"),
                       url(r'^(\d+)', "acorta.views.redirect"),
                       url(r'^.*', "acorta.views.notFound"),
                       )
