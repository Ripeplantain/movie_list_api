from django.shortcuts import render
from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def movie_list(request):
    
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)
    
    if request.method ==  "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



@api_view(['GET','PUT','DELETE'])
def movie_detail(request,pk):

    movie = Movie.objects.get(id=pk)


    if request.method == "GET":
        serializer = MovieSerializer(movie)

        return Response(serializer.data)
    
    if request.method  == "PUT":
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

    if request.method == "DELETE":
        movie.delete()
        return Response({
            "message":f"{movie.name} has been deleted from the database"
        })
