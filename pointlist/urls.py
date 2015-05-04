__author__ = 'ag'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from pointlist.views import account, homepage, register, create_post, login, sellers, buyers, profile

urlpatterns = patterns('',
                       url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
                       url(r'^$', homepage.bootstrap),
                       url(r'^register', register.SignUpView.as_view(), name="register"),
                       url(r'^create_post', create_post.CreatePostView.as_view(), name="create_post"),
                       url(r'^login', login.login_view, name="login"),
                       #url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': ''}),
                       url(r'^boots', homepage.bootstrap),
                       url(r'^profile', profile.profileView, name='profile'),
                       url(r'^buyers', buyers.boots, name='buyers'),
                       url(r'^sellers', sellers.boots, name='sellers'),
                       url(r'^parse_ajax', profile.parse_ajax, name='parse_ajax'),
)
