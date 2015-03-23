from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from sandbox.dash import views as dash

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sandbox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Dash
    url(r'^dash/$', dash.home, name='dash-home'),
