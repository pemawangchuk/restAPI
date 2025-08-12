from django.urls import path

from app.views import home, api_home

urlpatterns = [
    path('withoutapi', home, name='home'),  # Home view
    path('api/', api_home, name='api_home'),  # API home view
]