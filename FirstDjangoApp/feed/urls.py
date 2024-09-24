from django.urls import path
from .views import HomePageView

app_name = 'feed'
urlpattern = [path('',HomePageView.as_view(), name='index'),]
