from .models import Hashtag
from django.views import View
from django.shortcuts import render

# Create your views here.

class HashtagView(View):
    def get(self, request, hashtag, *args, **kwargs):
        obj, created = Hashtag.objects.get_or_create(tag=hashtag)
        return render(request, "hashtags/tag_view.html", {"obj":obj})
