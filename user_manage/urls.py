from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.sign_up, name='sign_up'),
    url(r'^signin/$', views.sign_in, name='sign_in'),
    url(r'^signout/$', views.sign_out, name='sign_out'),
    url(r'^self_profile/$', views.self_profile, name='self_profile'),
    url(r'^reset_pwd/$', views.reset_password, name='reset_password'),
    url(r'^mod_pwd/$', views.modify_password, name='modify_password'),
    url(r'^verify_user/$', views.verify_user, name='verify_user'),
    url(r'^send_activation_mail/(?P<username>\w+[-+.]?\w+)/$', views.activate_mail_send, name='send_activation_mail'),
    url(r'^activate=(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$', views.activate, name='activate')
]