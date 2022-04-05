from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from movie_app.models import Director, Movie, Review
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
def directors_list_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(director).data)


# @api_view(['GET'])
# def directors_list_view(request):
#     director = Director.objects.all()
#     data = DirectorSerializer(director, many=True).data
#     return Response(data=data)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(director)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(data={'massage': 'Director removed!'})
    else:
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data)


#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Product not found'})
#     data = DirectorSerializer(director).data
#     return Response(data=data)
#


@api_view(['GET', 'POST'])
def movie_list_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=title, description=description,
                                     duration=duration, director_id=director_id)
        return Response(data=MovieSerializer(movie).data)


# def movie_list_view(request):
#     movie = Movie.objects.all()
#     data = MovieSerializer(movie, many=True).data
#     return Response(data=data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(data={'massage': 'Movie removed!'})
    else:
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data=MovieSerializer(movie).data)


#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Product not found'})
#     data = MovieSerializer(movie).data
#     return Response(data=data)


@api_view(['GET', 'POST'])
def review_list_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text, movie_id=movie_id,
                                       stars=stars)
        return Response(data=ReviewSerializer(review).data)


# @api_view(['GET'])
# def review_list_view(request):
#     review = Review.objects.all()
#     data = ReviewSerializer(review, many=True).data
#     return Response(data=data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Product not found'})

    if request == 'GET':
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data)
    elif request == 'DELETE':
        review.delete()
        return Response(data={'massage': 'Review removed!'})
    else:
        review.text = request.data.get('text')
        review.movie = request.data.get('movie')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data)
    # data = ReviewSerializer(review).data
    # return Response(data=data)


@api_view(['GET'])
def movies_reviews_view(request):
    movie_reviews = Movie.objects.all()
    data = MovieSerializer(movie_reviews, many=True).data
    return Response(data=data)
