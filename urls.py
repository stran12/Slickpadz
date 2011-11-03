from django.conf.urls.defaults import *

# This is so that STATIC_URL will work
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'slickpadz.views.home', name='home'),
    # url(r'^slickpadz/', include('slickpadz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^properties/$', 'properties.views.properties'),
	(r'^search/$', 'properties.views.search'),
	(r'^api/$', 'properties.views.api'),
	(r'^$', 'properties.views.index'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


# This is also so that STATIC_URL will work
urlpatterns += staticfiles_urlpatterns()
