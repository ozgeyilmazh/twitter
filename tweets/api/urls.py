from django.conf.urls import url, include
from .views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='list'), # api/tweet/
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'), # api/tweet/create
    url(r'^(?P<pk>\d+)/$', TweetDetailAPIView.as_view(), name='detail'), # api/tweet/id/
    url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name='like'), # api/tweet/id/retweet
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'), # api/tweet/id/retweet
   
]
