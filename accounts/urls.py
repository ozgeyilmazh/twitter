from django.conf.urls import url, include
from .views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'), # /tweet/1
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollow.as_view(), name='follow'), # /tweet/1


]
