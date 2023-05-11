from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta
from .models import (
    Director,
    Movie,
    Review
)
from .serializers import (
    DirectorSerializer,
    MovieSerializer,
    ReviewSerializer,
    MovieReviewSerializer
                          )


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
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(DirectorSerializer(director).data)

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
        item.name = request.data.get('name')
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
        name = request.data.get('name')
        description = request.data.get('description')
        duration_str = request.data.get('duration')
        duration = timedelta(hours=int(duration_str.split(":")[0]), minutes=int(duration_str.split(":")[1]), seconds=int(duration_str.split(":")[2]))
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=name, description=description, duration=duration, director_id=director_id)
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
        item.title = request.data.get('name')
        item.description = request.data.get('description')
        duration_str = request.data.get('duration')
        duration_time = timedelta(hours=int(duration_str.split(":")[0]), minutes=int(duration_str.split(":")[1]), seconds=int(duration_str.split(":")[2]))
        item.duration = duration_time
        item.director_id = request.data.get('director_id')
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
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
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
        item.text = request.data.get('text')
        item.movie_id = request.data.get('movie_id')
        item.stars = request.data.get('stars')
        item.save()
        return Response(data=ReviewSerializer(item).data)