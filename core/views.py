from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from django.db.models import Q

def home(request):
    return render(request, "index.html")

User = get_user_model()
class SearchView(View):
    def get(self, request, *args, **kwargs):
        context = dict()
        query = request.GET.get('q')
        qs = None
        if query:
            qs = User.objects.filter(
                Q(username__icontains=query)
            )

        context["users"] = qs

        return render(request, 'search.html', context)

