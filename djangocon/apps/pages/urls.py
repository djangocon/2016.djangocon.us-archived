from django.conf.urls import url

from feeds import BlogFeed

urlpatterns = [
    url(r'^blog/feed/$', BlogFeed(), name='blog_feed'),
]