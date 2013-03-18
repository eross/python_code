from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
import app1.views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django1.views.home', name='home'),
    # url(r'^django1/', include('django1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^work/$',app1.views.work),
    url(r'^rpc/$',app1.views.rpc_handler),
    url(r'^callback/$',app1.views.callback),
    url(r'^listworkers/$',app1.views.listWorkers),
    url(r'^shutdown/$',app1.views.shutdown),
    url(r'^accounts/status/$',app1.views.login_status),
    url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout),

)
