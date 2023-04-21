from django.urls import path
from watchlist.api.views import *


urlpatterns = [
    path('all/', movie_list, name="movie_list"),
    path('<int:pk>/', movie_detail, name="movie_detail")
]