from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta
from .models import (
    Director,
    Movie,
    Review,
    Genre
)
from .serializers import (
    DirectorSerializer,
    DirectorValidateSerializer,
    MovieSerializer,
    MovieValidateSerializer,
    ReviewSerializer,
    ReviewValidateSerializer,
    MovieReviewSerializer,
    GenreSerializer,
    GenresValidateSerializer
                          )

@api_view(['GET', 'POST'])
def genre_list_api_view(request):
    if request.method == 'GET':
        genre_list = Genre.objects.all()
        genre_json = GenreSerializer(instance=genre_list, many=True).data
        return Response(data=genre_json)
    elif request.method == 'POST':
        serializer = GenresValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')
        genre = Genre.objects.create(name=name)
        return Response(data=GenreSerializer(genre).data)

@api_view(['GET', 'DELETE', 'PUT'])
def genre_detail_api_view(request, id):
    try:
        item = Genre.objects.get(id=id)
    except Genre.DoesNotExist:
        return Response(data={'error': 'Genre not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        genre_json = GenreSerializer(instance=item, many=False).data
        return Response(data=genre_json)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = GenresValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item.name = serializer.is_valid.get('name')
        item.save()
        return Response(data=GenreSerializer(item).data)

@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        """ List of objects = QuerySet """
        director_list = Director.objects.all()

        """ Reformat (Serialize) list of objects to DICT """
        director_json = DirectorSerializer(instance=director_list, many=True).data

        """ Return dict objects by JSON file """
        return Response(data=director_json)
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.is_valid.get('name')
        director = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(director).data)

@api_view(['GET', 'DELETE', 'PUT'])
def director_detail_api_view(request, id):
    """ Check object """
    try:
        item = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        """ Ads item serialize to dict """
        director_json = DirectorSerializer(instance=item, many=False).data

        """ Return dict by JSON file """
        return Response(data=director_json)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item.name = serializer.is_valid.get('name')
        item.save()
        return Response(data=DirectorSerializer(item).data)

@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        """ List of objects = QuerySet """
        movie_list = Movie.objects.all()

        """ Reformat (Serialize) list of objects to DICT """
        movie_json = MovieSerializer(instance=movie_list, many=True).data

        """ Return dict objects by JSON file """
        return Response(data=movie_json)
    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        # duration = timedelta(hours=int(duration_str.split(":")[0]), minutes=int(duration_str.split(":")[1]), seconds=int(duration_str.split(":")[2]))
        director_id = serializer.validated_data.get('director_id')
        genres = serializer.validated_data.get('genres')
        movie = Movie.objects.create(title=name, description=description, duration=duration, director_id=director_id)
        movie.genres.set(genres)
        return Response(data=MovieSerializer(movie).data)
@api_view(['GET'])
def movie_review_list_api_view(request):

    movie_review_list = Movie.objects.all()

    movie_review_json = MovieReviewSerializer(instance=movie_review_list, many=True).data

    return Response(data=movie_review_json)

@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail_api_view(request, id):
    """ Check object """
    try:
        item = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        """ Ads item serialize to dict """
        movie_json = MovieSerializer(instance=item).data

        """ Return dict objects by JSON file """
        return Response(data=movie_json)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item.title = serializer.validated_data.get('name')
        item.description = serializer.validated_data.get('description')
        # duration_str = request.data.get('duration')
        # duration_time = timedelta(hours=int(duration_str.split(":")[0]), minutes=int(duration_str.split(":")[1]), seconds=int(duration_str.split(":")[2]))
        item.duration = serializer.validated_data.get('duration')
        item.director_id = serializer.validated_data.get('director_id')
        item.save()
        return Response(data=MovieSerializer(item).data)
@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        """ List of objects = QuerySet """
        review_list = Review.objects.all()

        """ Reformat (Serialize) list of objects to DICT """
        review_json = ReviewSerializer(instance=review_list, many=True).data

        """ Return dict objects by JSON file """
        return Response(data=review_json)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.is_valid.get('text')
        movie_id = serializer.is_valid.get('movie_id')
        stars = serializer.is_valid.get('stars')
        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        return Response(data=ReviewSerializer(review).data)
@api_view(['GET', 'DELETE', 'PUT'])
def review_detail_api_view(request, id):
    """ Check object """
    try:
        item = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        review_json = ReviewSerializer(instance=item).data

        return Response(data=review_json)
    elif request.method == 'DELETE':
        item.delete()
        return Response(data=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item.text = serializer.is_valid.get('text')
        item.movie_id = serializer.is_valid.get('movie_id')
        item.stars = serializer.is_valid.get('stars')
        item.save()
        return Response(data=ReviewSerializer(item).data)