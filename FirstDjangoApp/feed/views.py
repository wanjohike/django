from django.shortcuts import render
from django .views.generic import TemplateView
from .models import Posts

class HomePageView(TemplateView):
    template_name = "index.html"


def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['posts'] = Posts.objects.all()
        return context

# Create your views here.
