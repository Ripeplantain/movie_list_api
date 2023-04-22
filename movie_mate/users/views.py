from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,generics
from .serializers import RegisterationSerializer

# Create your views here.


@api_view(['POST',])
def registeration_view(request):

    if request.method == "POST":

        serializer = RegisterationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            

def logout_view(request):

    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# class RegisterationView(generics.CreateAPIView):

#     serializer_class = RegisterationSerializer

    