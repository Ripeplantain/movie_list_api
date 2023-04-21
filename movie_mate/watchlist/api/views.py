from django.shortcuts import render
from watchlist.models import WatchList, StreamPlatform, Review
from watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status, generics

# Create your views here.


class CreateReviewAV(generics.CreateAPIView):

    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):

        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)

        review_queryset = Review.objects.filter(watchlist=movie, review_user=self.request.user)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")

        serializer.save(watchlist=movie)

class ListReviewAV(generics.ListAPIView):

    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



class StreamPlatformAV(APIView):

    def get(self,request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        


class StreamPlatformListAV(APIView):

    def get(self,request,pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self,request,pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def watch_list_view(request):
    
    if request.method == "GET":
        WatchLists = WatchList.objects.all()
        serializer = WatchListSerializer(WatchLists, many=True)

        return Response(serializer.data)
    
    if request.method ==  "POST":
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



@api_view(['GET','PUT','DELETE'])
def watch_list_detail(request,pk):

    watchList = WatchList.objects.get(id=pk)


    if request.method == "GET":
        serializer = WatchListSerializer(watchList)

        return Response(serializer.data)
    
    if request.method  == "PUT":
        serializer = WatchListSerializer(watchList,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

    if request.method == "DELETE":
        watchList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
