__author__ = 'ag'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from pointlist.views import account, homepage, register, create_post

urlpatterns = patterns('',
                       # url(r'^register', register.SignUpView.as_view(), name="register"),
                       # url(r'^home', homepage.WelcomeView.as_view(), name="welcome"),
                       # url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/pointlist/'}),
                       url(r'^$', homepage.bootstrap),
                       url(r'^register', register.SignUpView.as_view(), name="register"),
                       url(r'^create_post', create_post.CreatePostView.as_view(), name="create_post"),
)
