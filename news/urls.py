from django.urls import path

from news.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
]