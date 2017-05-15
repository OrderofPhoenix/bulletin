from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.sign_up, name='signup'),
    url(r'^signin/$', views.sign_in, name='signin'),
    url(r'^signout/$', views.sign_out, name='signout'),
    url(r'^self_profile/$', views.self_profile, name='selfprofile'),
    url(r'^find_pwd/$', views.find_password, name='findpwd'),
    url(r'^mod_pwd/$', views.modify_password, name='modpwd'),
    url(r'^verify_uid/$', views.verify_uid, name='verifyuid'),
    url(r'^activation_mail_send/(?P<username>\w+)/$', views.activate_mail_send, name='activationmailsend'),
    url(r'^activate=(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$', views.activate, name='activate')
]