from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^testproject/', include('testproject.foo.urls')),
    (r'simple', include('testproject.simple.urls')),
    (r'begin', 'simple.views.begin'),
    (r'longscroll', 'simple.views.longscroll'),
    (r'nojs', 'simple.views.nojs'),
    (r'html5', 'simple.views.html5'),
    (r'popup', 'simple.views.popup'),
    (r'frame_a', 'simple.views.frame_a'),
    (r'frame_b', 'simple.views.frame_b'),
    (r'', 'simple.views.index'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
