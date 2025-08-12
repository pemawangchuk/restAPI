from django.urls import path

from app.views import HomeView, home, api_home

urlpatterns = [
    path('withoutapi', home, name='home'),  # Home view
    path('api/', api_home, name='api_home'),  # API home view
    path('apiCDB/', HomeView.as_view(), name='api_home_class_based'),  # Class-based API home view
]