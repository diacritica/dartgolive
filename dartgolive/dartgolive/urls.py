from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from web import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dartgolive.views.home', name='home'),

    (r'^12345/$',views.launchProject),
    (r'^54321/$',views.checkLaunch),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += staticfiles_urlpatterns()
