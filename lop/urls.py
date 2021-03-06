from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('',
                       # home urls
                       url(r'^$',
                           'home.views.home',
                           name='home'),

                       # authentication app urls
                       url(r'^login',
                           'authentication.views.login',
                           name='login'),

                       url(r'^register',
                           'authentication.views.register',
                           name='register'),

                       url(r'^activation/(?P<token_id>.*)',
                           'authentication.views.activation',
                           name='activation'),

                       url(r'^logout$',
                           'authentication.views.logout',
                           name='logout'),

                       url(r'^new-image$',
                           'adminInterface.views.newimage',
                           name='newimage'),
                       )


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$',
                             'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

if settings.DEBUG:   # if DEBUG is True it will be served automatically
    urlpatterns += patterns('',
                            url(r'^static/(?P<path>.*)$',
                                'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                            )