from django.urls import path
from watchlist.api.views import *


urlpatterns = [
    path('all/', watch_list_view, name="movie_list"),
    path('<int:pk>/', watch_list_detail, name="movie_detail"),

    path('stream/', StreamPlatformAV.as_view(), name="stream"),
    path('stream/<int:pk>/', StreamPlatformListAV.as_view(), name="stream_detail"),

    path('stream/<int:pk>/review-create/', CreateReviewAV.as_view(), name="create_review"),
    path('stream/<int:pk>/review-list/', ListReviewAV.as_view(), name="list_review"),
    path('stream/review/<int:pk>/', ReviewDetailAV.as_view(), name="review_detail"),
]