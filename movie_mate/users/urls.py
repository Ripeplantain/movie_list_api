from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *


urlpatterns = [
    path('login/', obtain_auth_token, name="login"),
    # path('register/', registeration_view, name="register"),
    # path('register/', RegisterationView.as_view(), name="register"),
]