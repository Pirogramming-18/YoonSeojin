from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('movies/create', views.movie_create),
]