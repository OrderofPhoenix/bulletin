from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^create_bulletin/$', views.create_bulletin, name='create_bulletin'),
    url(r'^browse_bulletins/$', views.browse_bulletins, name='browse_bulletins'),
    url(r'^post_notice/(?P<bid>[0-9]+)/$', views.post_notice, name='post_notice'),
    url(r'^browse_notices/(?P<bid>[0-9]+)/$', views.browse_notices_by_bulletin, name='browse_notices'),
    url(r'^notice/(?P<nid>[0-9]+)/$', views.get_notice_detail_and_comment, name='browse_notice'),
    url(r'^search_bulletin/$', views.search_bulletin, name='search_bulletin'),
    url(r'^my_bulletin/$', views.my_bulletin, name='my_bulletin'),
    url(r'^follow_bulletin/(?P<bid>[0-9]+)/$', views.follow_bulletin, name='follow_bulletin'),
    url(r'^unfollow_bulletin/(?P<bid>[0-9]+)/$', views.unfollow_bulletin, name='unfollow_bulletin'),
    url(r'^delete_bulletin/(?P<bid>[0-9]+)/$', views.delete_bulletin, name='delete_bulletin'),
    url(r'^delete_notice/(?P<nid>[0-9]+)/$', views.delete_notice, name='delete_notice'),
    url(r'^remove_comment/(?P<nid>[0-9]+)/$', views.remove_comment, name='remove_comment'),

]