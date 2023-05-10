from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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


@api_view(['GET'])
def director_list_api_view(request):
    """ List of objects = QuerySet """
    director_list = Director.objects.all()

    """ Reformat (Serialize) list of objects to DICT """
    director_json = DirectorSerializer(instance=director_list, many=True).data

    """ Return dict objects by JSON file """
    return Response(data=director_json)

@api_view(['GET'])
def director_detail_api_view(request, id):
    """ Check object """
    try:
        item = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)

    """ Ads item serialize to dict """
    director_json = DirectorSerializer(instance=item, many=False).data

    """ Return dict by JSON file """
    return Response(data=director_json)

@api_view(['GET'])
def movie_list_api_view(request):
    """ List of objects = QuerySet """
    movie_list = Movie.objects.all()

    """ Reformat (Serialize) list of objects to DICT """
    movie_json = MovieSerializer(instance=movie_list, many=True).data

    """ Return dict objects by JSON file """
    return Response(data=movie_json)

@api_view(['GET'])
def movie_review_list_api_view(request):

    movie_review_list = Movie.objects.all()

    movie_review_json = MovieReviewSerializer(instance=movie_review_list, many=True).data

    return Response(data=movie_review_json)

@api_view(['GET'])
def movie_detail_api_view(request, id):
    """ Check object """
    try:
        item = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)

    """ Ads item serialize to dict """
    movie_json = MovieSerializer(instance=item).data

    """ Return dict objects by JSON file """
    return Response(data=movie_json)

@api_view(['GET'])
def review_list_api_view(request):
    """ List of objects = QuerySet """
    review_list = Review.objects.all()

    """ Reformat (Serialize) list of objects to DICT """
    review_json = ReviewSerializer(instance=review_list, many=True).data

    """ Return dict objects by JSON file """
    return Response(data=review_json)

@api_view(['GET'])
def review_detail_api_view(request, id):
    """ Check object """
    try:
        item = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

    review_json = ReviewSerializer(instance=item).data

    return Response(data=review_json)
