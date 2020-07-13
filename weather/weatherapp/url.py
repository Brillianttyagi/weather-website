from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('fetchweather',views.fetchweather,name="fetchweather")
]