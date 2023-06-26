
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about" ),
    path('about_aqi.html', views.about_aqi, name="AQI"),
]